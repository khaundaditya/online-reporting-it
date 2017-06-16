from django.conf.urls import url
from . import views
from reports.views import *
from reviewer.views import *
from django_messages.views import *
urlpatterns = [

	#url(r'^login/$',views.user_login,name='login')

	#login/logout URLS
	url(r'^login/$', 'django.contrib.auth.views.login',name='login'),

	url(r'^logout/$', 'django.contrib.auth.views.logout',name='logout'),
	url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login',name='logout_then_login'),
	url(r'^$', views.dashboard, name='dashboard'),
	#Password Change URLs
	url(r'^password-change/$','django.contrib.auth.views.password_change',name='password_change'),
	url(r'^password-change/done/$','django.contrib.auth.views.password_change_done',name='password_change_done'),

	#Password Reset URLs
	url(r'^password-reset/$','django.contrib.auth.views.password_reset',name='password_reset'),
	url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done',name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
	'django.contrib.auth.views.password_reset_confirm',
	name='password_reset_confirm'),
	url(r'^password-reset/complete/$',
	'django.contrib.auth.views.password_reset_complete',
	name='password_reset_complete'),
	#Registation URL
	url(r'^register/$',views.register,name='register'),
	
	#Other Apps
	#Applicant Side

	# url(r'^hardware/$',generateHardwareReport,name='hardware'),
	# url(r'^manpower/$',generateManpowerReport,name='manpower'),
	# url(r'^csc/$',generateCSCReport,name='csc'),
	# url(r'^swan/$',generateSWANReport,name='swan'),
	# url(r'^digital_literacy/$',generateDLReport,name='digital_literacy'),
	# url(r'^nofn/$',generateNOFNeport,name='nofn'),
	# url(r'^software/$',generateSoftwareReport,name='software'),
	# url(r'^g2cservice/$',generateG2CServiceReport,name='g2cservice'),
	# url(r'^edist_transaction/$',generateeDistrictTransactionReport,name='edist_transaction'),

	url(r'^generate_report/$',generateReport,name='generate_report'),
	#url(r'^populate_comment/$',populateComment,name='populate_comment'),
	#url(r'^reviewer_comment/$',handleComments,name='reviewer_comment'),
	#url(r'^update_manpower_snapshot/$',updateManpowerReport,name='update_manpower_snapshot'),
	url(r'^edit/(?P<reportname>\w+)/$', edit_report,name='edit_report'),
	url(r'^generate/(?P<reportname>\w+)/$', generate_report,name='generate_report'),
	url(r'^delete/$', delete_report,name='delete_report'),
	url(r'^analyze_report/(?P<reportname>\w+)/$',analyze_report,name='analyze_report'),
	url(r'^read_from_excel/(?P<reportname>\w+)/$', uploadXL_File_ToDB,name='read_from_excel'),
	#Third party
	url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/$', compose, name='messages_compose'),
    url(r'^compose/(?P<recipient>\w+)/$', compose,name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', view, name='messages_detail'),
    url(r'^delete/(?P<message_id>[\d]+)/$', delete, name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', undelete, name='messages_undelete'),
    url(r'^trash/$', trash, name='messages_trash'),
]

