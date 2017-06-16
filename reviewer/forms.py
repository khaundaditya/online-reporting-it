from django import forms
#from .models import Comment
#from .models import DISTRICT_CHOICES
from mysite.custom_config import *
class ReportForm(forms.Form):

    district = forms.ChoiceField(choices=DISTRICT_CHOICES,label="District")
    report_name = forms.ChoiceField(choices=REPORT_NAMES,label="Report Name")
    #YYYYMM= forms.CharField(required=True,label="YYYYMM")
    year= forms.ChoiceField(choices=YEAR_CHOICES,label="Year")
    month= forms.ChoiceField(choices=MONTH_CHOICES,label="Month")

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')
class AnalyzeReportForm(forms.Form):
  
  def __init__(self, choices, *args, **kwargs):
      super(AnalyzeReportForm, self).__init__(*args, **kwargs)
      self.fields['analysis_type'] = forms.ChoiceField(choices=choices)



