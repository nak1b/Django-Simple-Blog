from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

from . import models

class EntryAdmin(MarkdownModelAdmin):
	list_display = ("title", "created", "published")
	prepopulated_fields = {"slug": ("title",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}



# class PostAdmin(admin.ModelAdmin):
# 	list_display = ("title", "created", "published")
# 	prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.PostEntry, EntryAdmin)
# Register your models here.
