# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Project

class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('name','staff','project_date')

admin.site.register(Project,ProjectAdmin)
    #ProjectAdmin)

# Register your models here.
