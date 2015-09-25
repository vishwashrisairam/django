from django.contrib import admin
from .models import *
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

# Register your models here.
class EntryAdmin(MarkdownModelAdmin):
	list_display=("title","created")
	prepopulated_fields={"slug":("title",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

	

admin.site.register(Entry,EntryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)