from .forms import *
from mysite import custom_config
MODEL_FORM_BY_MODELNAME  = {
	
	'ManpowerReport' : ManpowerReportForm,
	'HardwareReport' : HardwareReportForm,
	'CSCReport' : CSCReportForm,
	'SWANReport' : SWANReportForm,
	'DLReport' : DigitalLiteracyReportForm,
	'NOFNReport': NOFNReportForm,
	'SoftwareReport' :  SoftwareReportForm,
	'g2cServiceReport' : G2CServiceReportForm,
	'ServiceTransReport' : eDistrictReportForm,
	
}
REPORT_TEMPLATES= {

	
	'Manpower' : 'reports/manpower.html',
	'CSC': 'reports/csc.html',
	'SWAN' : 'reports/swan.html',
	'Software' : 'reports/software.html',
	'Hardware' : 'reports/hardware.html',
	'DL' : 'reports/digital_literacy.html',
	'NOFN' : 'reports/nofn.html',
	'g2cService' : 'reports/g2c_service.html',
	'ServiceTrans' : 'reports/edistrict_transaction.html'

}
def get_verbose_report_month(report_month,flag):
	outstr = ''
	if report_month:
		year = report_month[0:4]
		month = report_month[4:6]
		# if flag == 'edit':
		# 	print custom_config.month_dict
		# 	v_month = custom_config.month_dict[month]
		# 	outstr = v_month + ',' + year
		# elif flag == 'generate':
		v_month = custom_config.month[month]
		outstr = v_month + ',' + year

	return outstr