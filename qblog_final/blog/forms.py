from django import forms
from .models import *
from django.contrib.auth.models import User


class EntryForm(forms.ModelForm):
	class Meta:
		model=Entry
		exclude=["publish",]
	
class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		exclude=["post","author",]

	