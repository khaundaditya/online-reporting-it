from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
#Custom Classes
from .forms import *
from reports.forms import *
from reviewer.models import *

@login_required
def dashboard(request):
	group = ''
	status = ''
	queryset = Comment.objects.all()
	if request.user.groups.filter(name="Reviewer").exists():
		group = 'Reviewer'
		status = 'raised'
	elif request.user.groups.filter(name="Applicant").exists():
		group = 'Applicant'
		status = 'reverted'
	elif request.user.groups.filter(name="Administrators").exists():
		group = 'Administrators'
		status = 'NA'

	return render(request,'account/dashboard.html',
							{'section': 'dashboard','group':group,'status':status,'user':request.user} )


def register(request):
	if request.method == 'POST':
		####
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			new_user.groups.add(Group.objects.get(name='Applicant'))
			return render(request,'account/register_done.html',{'new_user':new_user})
	else:
		user_form = UserRegistrationForm()

	return render(request,'account/register.html',{'user_form':user_form})

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])

			if user is not None:
				#request.session['username'] = username
				if user.is_active:
					login(request,user)
					return HttpResponse('Authenticated Successully')
				else:
					return HttpResponse('Disabled Account')
			else:
				return HttpResponse('Invalid Login')

	else:
		form = LoginForm()

	return render (request,'account/login.html',{'form':form,'user':request.user})
# Create your views here.
