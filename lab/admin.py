# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Project,Sample

class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('name','staff','project_date')
    list_filter = ['project_date']
    search_fields = ['name','description']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Sample)

