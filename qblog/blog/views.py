from django.views import generic
from django.shortcuts import render,redirect
from . import models
from .forms import EntryForm


# Create your views here.
class BlogIndex(generic.ListView):
	queryset=models.Entry.objects.published()
	template_name="blog/home.html"
	paginate_by=3

class BlogDetail(generic.DetailView):
	model=models.Entry
	template_name="blog/post.html"	


def new(request):
	form= EntryForm()
	if request.method=="POST":
		form=EntryForm(request.POST)
		if form.is_valid():
			post=form.save()
			return redirect('/')
		form=EntryForm()	

	return render(request,'blog/write.html',{'form':form})