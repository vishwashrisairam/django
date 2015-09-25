from django.db import models
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
	slug=models.SlugField(max_length=200,unique=True)

	def __str__(self):
		return self.slug

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Entry(models.Model):
	title=models.CharField(max_length=155)
	body=MarkdownField()
	slug=models.SlugField(unique=True)
	publish=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)
	tags=models.ManyToManyField(Tag)

	objects=EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("entry_detail",kwargs={"slug":self.slug})	

	class Meta:
		verbose_name="Blog Entries"
		verbose_name_plural="Blog Entries"
		ordering=["-created"]		
