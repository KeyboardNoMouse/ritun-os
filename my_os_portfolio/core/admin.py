from django.contrib import admin # This was 'django.db', changed to 'django.contrib'
from .models import Project,Document

admin.site.register(Project)
admin.site.register(Document)