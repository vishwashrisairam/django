from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail 
from django.conf import settings
from .models import SignUp
from forms import *


# Create your views here.
def signup(request):
	form=SignUpForm(request.POST or None)
	if form.is_valid():
		save_it=form.save(commit =False)
		save_it.save()
		subject='Email confirmation'
		message='Welcome to abc.com.Click on the link to activate your account link'
		from_email=settings.EMAIL_HOST_USER
		to_list=[save_it.email,settings.EMAIL_HOST_USER]
		send_mail(subject,message,from_email,to_list,fail_silently=True)
		messages.success(request,'We will be in touch ')
		return HttpResponseRedirect('/thank-you')
	return render(request,'signups/signups.html',{'form':form})

def thankyou(request):
	return render(request,'signups/thankyou.html',{})

def aboutus(request):
	return render(request,'signups/aboutus.html',{})	
