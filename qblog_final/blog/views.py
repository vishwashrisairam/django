from django.views import generic
from django.shortcuts import render,render_to_response,redirect,get_object_or_404,RequestContext
from . import models
from .forms import EntryForm,CommentForm


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

def single_post(request, slug):
    post = get_object_or_404(models.Entry, slug=slug)
    comments=post.comment_set.all()
    form=CommentForm()
    if request.method=="POST":
    	form=CommentForm(request.POST)
    	if form.is_valid():
    		comment=form.save(commit=False)
    		comment.post=post
    		comment.author=request.user
    		comment.save()
    		return redirect('/'+slug+'/')
    return render_to_response('blog/single.html', locals(), context_instance=RequestContext(request))






