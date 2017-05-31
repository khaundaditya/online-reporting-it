from django.conf.urls import url
from . import views
from django_messages.views import *

urlpatterns = [
	
	url(r'^generate_report/$',views.generateReport,name='generate_report'),
	url(r'^generate_PDF/$',views.generatePDF,name='generate_pdf'),
	url(r'^generate_XLS/$',views.generateXLS,name='generate_XLS'),
	url(r'^generate_XLSX/$',views.generateXLSX,name='generate_XLSX'),
	url(r'^analyze_report/$',views.analyze_report,name='analyze_report'),
	url(r'^reviewer_comment/$',views.handleComments,name='reviewer_comment'),
	url(r'^populate_comment/$',views.populateComment,name='populate_comment'),
	url(r'^populate_snapshot/$',views.populateSnapshot,name='populate_snapshot'),

	#URL Django Messages
	
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