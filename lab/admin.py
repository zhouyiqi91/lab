# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from models import *

def is_manage(user):
    return user.groups.filter(name='manage').exists()

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = '部门'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, ) 
    #list_display=['username']

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('name','staff','project_type','project_date',)
    list_filter = ['project_date']
    search_fields = ['name','description']


    # 只能看到自己项目
    def get_queryset(self, request):
        if request.user.is_superuser or is_manage(request.user) :
            return Project.objects.all()
        return Project.objects.filter(people__user=request.user)

admin.site.register(Project,ProjectAdmin)

class SampleAdmin(admin.ModelAdmin):

    list_display = ('name','staff','sample_date','library','view_link')
    list_filter = ['sample_date']
    search_fields = ['name','description']

    # 只能看到自己项目的样本
    def get_queryset(self, request):
        if request.user.is_superuser or is_manage(request.user) :
            return Sample.objects.all()
        return Sample.objects.filter(project__people__user=request.user)

    # 只能添加自己项目的样本 
    def get_form(self, request, obj=None, **kwargs):
        form = super(SampleAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['project'].queryset = Project.objects.filter(people__user=request.user)
        return form

admin.site.register(Sample,SampleAdmin)

