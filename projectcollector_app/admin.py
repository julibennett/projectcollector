from django.contrib import admin

from .models import Project, Feedback, Tag

# Register your models here.

admin.site.register(Project)
admin.site.register(Feedback)
admin.site.register(Tag)
