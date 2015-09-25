from django.shortcuts import render_to_response, RequestContext, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.
def all_posts(request):
	post_list=Post1.objects.all()
	paginator=Paginator(post_list,6)
	page=request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		posts=paginator.page(1)	
	except EmptyPage:
		posts=paginator.page(paginator.num_pages)

	return render_to_response('blog/all.html',locals(),context_instance=RequestContext(request))		

def single_post(request, slug):
    post = get_object_or_404(Post1, slug=slug)
    return render_to_response('blog/single.html', locals(), context_instance=RequestContext(request))

def category_archive(request,slug):
	category=get_object_or_404(Category,slug=slug)
	categories=Category.objects.all()
	posts=Post1.objects.filter(categories=category)
	return render_to_response('blog/category.html',locals(),context_instance=RequestContext(request))    	

