from django import forms
#from parsley.decorators import parsleyfy
from mysite.custom_config import *
from .models import *


class ManpowerReportForm(forms.ModelForm):


	class Meta:
		model = ManpowerReport
		exclude = ('updated_date','user_name','report_month')

class HardwareReportForm(forms.ModelForm):

	class Meta:
		model = HardwareReport
		exclude = ('updated_date','user_name','report_month')
class CSCReportForm(forms.ModelForm):
	class Meta:
		model = CSCReport
		exclude = ('updated_date','user_name','report_month')

class SWANReportForm(forms.ModelForm):
	class Meta:
		model = SWANReport
		exclude = ('updated_date','user_name','report_month')

class DigitalLiteracyReportForm(forms.ModelForm):
	class Meta:
		model = DLReport
		exclude = ('updated_date','user_name','report_month')


class NOFNReportForm(forms.ModelForm):
	class Meta:
		model = NOFNReport
		exclude = ('updated_date','user_name','report_month')

class SoftwareReportForm(forms.ModelForm):
	class Meta:
		model = SoftwareReport
		exclude = ('updated_date','user_name','report_month')
class G2CServiceReportForm(forms.ModelForm):
	class Meta:
		model = g2cServiceReport
		exclude = ('updated_date','associated_line_department','user_name','report_month')
class eDistrictReportForm(forms.ModelForm):
	class Meta:
		model = ServiceTransReport
		exclude = ('updated_date','associated_line_department','user_name','report_month')
class UpdateSnapshotForm(forms.Form):

	district = forms.ChoiceField(choices=DISTRICT_CHOICES,label="District")
	#YYYYMM= forms.CharField(required=True,label="Report Month")
	year= forms.ChoiceField(choices=YEAR_CHOICES,label="Year")
	month= forms.ChoiceField(choices=MONTH_CHOICES,label="Month")
class DeleteReportForm(forms.Form):
	district = 	forms.ChoiceField(choices=DISTRICT_CHOICES,label="District")
	#YYYYMM = forms.CharField(required=True,label="YYYYMM")
	year= forms.ChoiceField(choices=YEAR_CHOICES,label="Year")
	month= forms.ChoiceField(choices=MONTH_CHOICES,label="Month")
	report_name = forms.ChoiceField(choices=REPORT_NAMES,label="Report Name")
class ImportExcelForm(forms.Form):
	district = 	forms.ChoiceField(choices=DISTRICT_CHOICES,label="District")
	file_type = forms.ChoiceField(choices=FILE_UPLOAD_CHOICES,label="FileType")
	file  = forms.FileField(label= "Choose excel to upload")