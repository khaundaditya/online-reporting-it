from django.conf.urls import url
from . import views


urlpatterns = [
	
	# url(r'^hardware/$',views.generateHardwareReport,name='hardware'),
	# url(r'^manpower/$',views.generateManpowerReport,name='manpower'),
	# url(r'^csc/$',views.generateCSCReport,name='csc'),
	# url(r'^swan/$',views.generateSWANReport,name='swan'),
	# url(r'^digital_literacy/$',views.generateDLReport,name='digital_literacy'),
	# url(r'^nofn/$',views.generateNOFNeport,name='nofn'),
	# url(r'^software/$',views.generateSoftwareReport,name='software'),
	# url(r'^g2cservice/$',views.generateG2CServiceReport,name='g2cservice'),
	# url(r'^edist_transaction/$',views.generateeDistrictTransactionReport,name='edist_transaction'),
	#url(r'^update_manpower_snapshot/$',views.updateManpowerReport,name='update_manpower_snapshot'),
	url(r'^edit/(?P<reportname>\w+)/$', views.edit_report,name='edit_report'),
	url(r'^generate/(?P<reportname>\w+)/$', views.generate_report,name='generate_report'),
	url(r'^read_from_excel/(?P<reportname>\w+)/$', views.uploadXL_File_ToDB,name='read_from_excel'),
	url(r'^delete/$', views.delete_report,name='delete_report'),
	url(r'^logs/$', views.show_activity_logs,name='logs'),
	#url(r'^edit_manpower/$',views.edit_manpower,name='edit_manpower'),
	#url(r'^manpower/$', 'formset', {'formset_class': ContactFormset, 'template': 'example/formset-table.html'}, name='example_table'),

]
