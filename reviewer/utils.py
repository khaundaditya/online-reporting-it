from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from mysite import custom_config
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def _get_verbose_report_month(report_month):
	outstr = ''
	if report_month:
		year = report_month[0:4]
		month = report_month[4:6]
		v_month = custom_config.month[month]
		outstr = v_month + ',' + year


	return outstr