from .forms import *
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