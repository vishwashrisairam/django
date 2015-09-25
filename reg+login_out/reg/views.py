from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	return render(request,'reg/base.html',{})


def register(request):
	context = RequestContext(request)
	registered=False
	if request.method=='POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()

			profile=profile_form.save(commit=False)
			profile.user=user

			registered=True
		else:
			print user_form.errors,profile_form.errors
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()
	return render_to_response(
            'reg/register.html',
            {'user_form': user_form, 'profile_form': profile_form,'registered': registered},
            context )				
def user_login(request):
	context=RequestContext(request)
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Your account is disabled')	
		else:
			return HttpResponse('Invalid login credentials')

	else:
		return render_to_response('reg/login.html',{},context)				

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
