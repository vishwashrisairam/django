from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class PostManager(models.Manager):
	def all(self):
		return super(PostManager,self).filter(publish=True)	

class Category(models.Model):
	title=models.CharField(max_length=50)
	slug=models.SlugField(unique=True)
	description=models.TextField(max_length=155)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category',args=[str(self.slug)])

class Post(models.Model):
	publish=models.BooleanField(default=False)
	author=models.ForeignKey(User)
	categories=models.ManyToManyField(Category)
	title = models.CharField(max_length=65)
	slug=models.SlugField(unique=True)
	description=models.TextField(max_length=155)
	content=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	objects=PostManager()

	class Meta:
		ordering=['-timestamp',]

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('post',args=[str(self.slug)])

	def get_previous_post(self):
		return self.get_previous_by_timestamp()

	
	def get_next_post(self):
		return self.get_next_by_timestamp()	

class Post1(models.Model):
	title=models.CharField(max_length=65)
	body=models.TextField()
	date=models.DateTimeField(auto_now_add=True,auto_now=False)
	slug=models.SlugField(unique=True)

	def __str__(self):
		return	self.title

	def get_absolute_url(self):
		return reverse('post',args=[str(self.slug)])
							