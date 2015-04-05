from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "created", "published")
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.PostEntry, PostAdmin)
# Register your models here.
