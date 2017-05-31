from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import mail_admins
from django.contrib import messages
from django.forms.formsets import formset_factory
#from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.forms.models import modelformset_factory
#from django.db.models.loading import get_model
from django.db import IntegrityError
from django.db.models import Q
from django.contrib import messages
from django.conf import settings

import os
import re

from .forms import *
from .utils import *
#from .models import HardwareReport,ManpowerReport,CSCReport,HardwareReport,SWANReport,DigitalLiteracyReport,NOFNReport,SoftwareReport
from django.contrib.auth.decorators import login_required
from reviewer.models import *
from .models import *
from mysite import custom_config
from reports import models

#from .models import HardwareReport
# Create your views here.
district_dict = dict(DISTRICT_CHOICES)


@login_required
def edit_report(request,reportname=None):
	report_name = reportname
	reportname = _getCustomReportName(reportname)
	parent_templ = REPORT_TEMPLATES[report_name]
	a_form = UpdateSnapshotForm()
	model = report_name +'Report'
	#model_obj = get_model('reports', model)
	model_obj = getattr(models, model)
	YYYYMM = ''
	district = ''
	#ModelFormset = modelformset_factory(model_obj,exclude=ManpowerReportForm.Meta.exclude,extra=0)
	ModelFormset = modelformset_factory(model_obj,form=MODEL_FORM_BY_MODELNAME[model],extra=0)
	formset = ModelFormset(queryset=model_obj.objects.none())
	if request.method == 'POST':
		a_form = UpdateSnapshotForm(request.POST)
		formset = ModelFormset(request.POST)
		timestamp  = timezone.now()
		today_date=timestamp.strftime('%Y%m%d')
		if a_form.is_valid():
			if 'genvalue' in request.POST:
				YYYYMM = a_form.cleaned_data['YYYYMM']
				district = a_form.cleaned_data['district']
				district_full_name = district_dict[district]
				
				#filtered_result = _getFilteredQuerySetForEdit(reportname,YYYYMM,district)
				#formset = ModelFormset(queryset=ManpowerReport.objects.filter(Q(district=district), Q(updated_date__contains=YYYYMM)) )
				resultset=model_obj.objects.filter(Q(district=district), Q(report_month=YYYYMM))
				formset = ModelFormset(queryset=resultset )
				if not resultset.exists():
					msg = 'No submitted data available for selected district: ' + district_dict[district]  + ' for reporting month: ' + YYYYMM
					return render(request,'reports/status.html',{'msg': msg,'error':1} )
				
				context = {'formset': formset,'update':1,'a_form': a_form,'show':1 ,'YYYYMM':YYYYMM,'district':district,'reportname': reportname,'parent_template':parent_templ}
				return render(request,'reports/edit.html',context)
			elif 'updateid' in request.POST:
				YYYYMM = request.POST.get("YYYYMM", "")
				district = request.POST.get("district", "")
				#print ("U " + YYYYMM + ' ' + district)
				if   formset.is_valid():
					for f_form in formset:
						if f_form.is_valid() and f_form.has_changed():
					       		cd = f_form.cleaned_data
					    		#print cd
					    		instance = f_form.save(commit=False)
					    		instance.updated_date = today_date
					    		instance.user_name = str(request.user)
					    		instance.report_month = YYYYMM
					    		instance.district = district
					    		if report_name == 'g2cService' or report_name == 'ServiceTrans':
									service_nm = cd['service_nm']
									if service_nm:
										instance.associated_line_department = SERVICE_TO_DEPARTMENT_MAP[service_nm]
									else:
										instance.associated_line_department = 'NA'
							instance.save()

					_updateSnapshot(request.user,report_name,YYYYMM,district)	
					msg = reportname + " Report has been successfully updated"		
					log_obj = LogActivity(user=request.user,report_name=reportname,district=district_dict[district],
									submitted_time=timezone.now(),message='Updation of existing Report')
					log_obj.save()
					#return HttpResponse('Hello')
					return render(request,'reports/status.html',{'success':1,'msg':msg})
					    		
				else:
					print formset.errors
					
					

	context = {'formset': formset,'update':1,'a_form': a_form,'reportname' : reportname,'parent_template':parent_templ }
	return render(request,'reports/edit.html',context)


@login_required
def show_activity_logs(request):
	#snapshot=ReportSnapShot.objects.filter( Q(district=district), Q(state='submitted')|Q(state='inprogress'), Q(owner=user), Q(report_type=report_type) )
	if request.user.groups.filter( Q(name='Reviewer')|Q(name='Adminstrators') ).exists():
		log_list = LogActivity.objects.all().order_by('-submitted_time','district')[:30]
	elif request.user.groups.filter( Q(name='Applicant') ).exists():
		log_list = LogActivity.objects.filter(user=request.user).order_by('-submitted_time')
	return render(request,'reports/show_activity_logs.html',{'log_list':log_list})
@login_required
def generate_report(request,reportname=None):

	report_name = reportname
	reportname = _getCustomReportName(reportname)
	model = report_name +'Report'
	context = {}
	#model_obj = get_model('reports', model)
	model_obj = getattr(models, model)
	DataFormset =  formset_factory(MODEL_FORM_BY_MODELNAME[model],extra=1)
	if request.method == 'POST':
		formset = DataFormset(request.POST)
		today_date = _getTodayDate()
		report_month = today_date[0:6]
		com_dist = ''
		if formset.is_valid():
			com_dist = ''
			for f_form in formset:
				cd = f_form.cleaned_data
				dist = cd['district']
				if not dist:
					dist = com_dist
				else:
					com_dist = dist
				#print (cd)
				instance = f_form.save(commit=False)
				instance.user_name = str(request.user)
				instance.updated_date = today_date
				instance.report_month = report_month
				instance.district = com_dist
				if report_name == 'g2cService' or report_name == 'ServiceTrans':
					service_nm = cd['service_nm']
					if service_nm:
						instance.associated_line_department = SERVICE_TO_DEPARTMENT_MAP[service_nm]
					else:
						instance.associated_line_department = 'NA'

				try:
						# if _isReportInProgress(com_dist,request.user,report_name):
						# 	msg = "your previous submission for "+ reportname + " report hasn't yet be closed.New data willn't be saved"
						# 	messages.warning(request, msg)
						# 	print(msg)
						# 	return render(request,'reports/status.html',{'messages':messages,'msg':msg,'error':1})
						# else:
						instance.save()		
				except IntegrityError:
						msg = 'Similar set of data already submitted today.Hence can\'t be re-submitted'
						print(msg)
						messages.error(request, msg)
						return render(request,'reports/status.html',{'msg':msg,'error':1})
			_updateSnapshot(request.user,report_name,report_month,com_dist)
			msg = reportname + " Report has been successfully submitted"

			log_obj = LogActivity(user=request.user,report_name=reportname,district=district_dict[com_dist],
									submitted_time=timezone.now(),message='New Submission')
			log_obj.save()
			return render(request,'reports/status.html',{'success':1,'msg':msg})
		else:
			print "Invalid Formset"
			print formset.errors

	else:
		context = {'formset': DataFormset(),'new':1 }
	return render(request,REPORT_TEMPLATES[report_name],context)

@login_required
def delete_report(request):

	if request.method == 'POST':
		form = DeleteReportForm(request.POST)
		if form.is_valid():
			district = form.cleaned_data['district']
			district_full_name = district_dict[district]
			report_name = form.cleaned_data['report_name']
			YYYYMM = form.cleaned_data['YYYYMM']
			if report_name == 'DigitalLiteracy':
				report_name = 'DL'
			elif report_name == 'eDistrictTrans':
				report_name = 'ServiceTrans'
			elif report_name == 'G2CServices':
				report_name = 'g2cService'

			model = report_name + 'Report'
			model_obj = getattr(models,model)
			instance = model_obj.objects.filter(district=district,report_month=YYYYMM)
			if instance.exists():
				instance.delete()
			snapshot_obj = ReportSnapShot.objects.filter(district=district,report_type=report_name,YYYYMM=YYYYMM)
			if snapshot_obj.exists():
				msg = 'Data delete for report ' + report_name + ' for district ' + district_full_name + ' for month ' + YYYYMM
				return render(request,'reports/status.html',{'success':1,'msg':msg})
		else:
			print form.errors
	
	form = DeleteReportForm()
	context = {'form' : form}
	return render(request,'reports/delete_report.html',context)
 
"""
Private Helper Routines
"""

def _updateSnapshot(user,report_name,YYYYMM,district):
	model_name = report_name + 'Report'
	model_obj = getattr(models,model_name);
	reportname = _getCustomReportName(report_name)
	queryset = model_obj.objects.filter(district=district,report_month=YYYYMM)
	district_full_name = district_dict[district]
	context = {'filtered_result': queryset,\
	'report_name': report_name,'district': district,'YYYYMM':YYYYMM,'include_href':1,\
	'district_full_name':district_full_name,'override' : 1,'recipient':user }
	templ = _getTemplateFile(report_name)
	content = render_to_string(templ, context)
	#print (content)
	bin_content = _convertStringToByte(content)
	obj = ReportSnapShot.objects.filter(district=district,report_type=report_name,owner=user)
	if obj.exists():
		print("Updating Existing Snapshot")
		obj.content = b''
		obj.update(content=bin_content)
	else:
		Snapshot = ReportSnapShot(content=bin_content,owner=user,report_type=report_name,district=district,state='submitted',YYYYMM=YYYYMM)
		#try:
		Snapshot.save()

def _getTemplateFile(report_name):
	TEMPL_DIR = os.path.abspath(os.path.join(settings.PROJECT_DIR,'../reviewer/templates/reviewer'))
	templ_name = ''
	if report_name == 'Manpower':
		templ_name = TEMPL_DIR + '/mp.html'
	elif report_name == 'CSC':
		templ_name = TEMPL_DIR + '/csc.html'
	elif report_name == 'SWAN':
		templ_name = TEMPL_DIR + '/swan.html'
	elif report_name == 'NOFN':
		templ_name = TEMPL_DIR + '/nofn.html'
	elif report_name == '':
		templ_name = TEMPL_DIR + '/swan.html'
	elif report_name == 'Hardware':
		templ_name = TEMPL_DIR + '/hardware.html'
	elif report_name == 'Software':
		templ_name = TEMPL_DIR + '/software.html'
	elif report_name == 'DL':
		templ_name = TEMPL_DIR + '/digital_literacy.html'
	elif report_name == 'ServiceTrans':
		templ_name = TEMPL_DIR + '/edistrict_transaction.html'
	elif report_name == 'g2cService':
		templ_name = TEMPL_DIR + '/g2c_service.html'

	return templ_name

def _getFilteredResult(queryset,district,yyyymm):

	filtered_result = [ q for i,q in enumerate(queryset) if q.district==district and re.match(yyyymm,q.updated_date) ]

	return filtered_result
def _getTodayDate():
	timestamp  = timezone.now()
	return timestamp.strftime('%Y%m%d')


def _isReportInProgress(district,user,report_type):
	state = None
	try:
		snapshot=ReportSnapShot.objects.filter( Q(district=district), Q(state='submitted')|Q(state='inprogress'), Q(owner=user), Q(report_type=report_type) )
		if snapshot:
			state = True
		else:
			state = False
	except ReportSnapShot.DoesNotExist:	
		state = False

	return state
def _convertStringToByte(s):
	lst = []
	for ch in s:
		hv = hex(ord(ch)).replace('0x', '')
		if len(hv) == 1:
			hv = '0'+hv
		lst.append(hv)
	hex_str =''.join( lst )
	bytes = []

	hexStr = ''.join( hex_str.split(" ") )

	for i in range(0, len(hexStr), 2):
		bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

	return ''.join( bytes )


def _getCustomReportName(reportname):
	report = ''
	if reportname == 'DL':
		report = 'Digital Literacy'	
	elif reportname == 'g2cService':
		report = 'G2C Service'	
	elif reportname == 'ServiceTrans':
		report = 'e-District Transaction'
	else:
		report = reportname

	return report