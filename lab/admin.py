# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from models import *
from django.db.models import Q

def is_manage(user):
    return user.groups.filter(name='manage').exists()

def is_bioinfo(user):
    return user.groups.filter(name='bioinfo').exists()

def is_lab(user):
    return user.groups.filter(name='lab').exists()



"""
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
"""

class ProjectAdmin(admin.ModelAdmin):

    #exclude = ('project_id',)   
    list_display = ('name','lab_staff','project_type','project_date','sample_number','bioinfo_staff')
    #list_filter = ['project_date']
    search_fields = ['name','lab_staff','project_type','project_date','bioinfo_staff','description']


    # 只能看到自己项目
    
    def get_queryset(self, request):
        if request.user.is_superuser or is_manage(request.user) :
            return Project.objects.all()
        elif is_bioinfo(request.user):
            return Project.objects.filter(bioinfo_people=request.user)
        elif is_lab(request.user):
            return Project.objects.filter(lab_people=request.user) 
        # Q(created_by=request.user) | Q(bioinfo_people=request.user) |Q(created_by=request.user) )
    
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

admin.site.register(Project,ProjectAdmin)

class SampleAdmin(admin.ModelAdmin):

    list_display = ('name','p_id','sample_date','library','view_link')
    #list_filter = ['sample_date']
    search_fields = ['name','sample_date','library_id','description']

    # 只能看到自己项目的样本
    def get_queryset(self, request):
        if request.user.is_superuser or is_manage(request.user) :
            return Sample.objects.all()
        elif is_lab(request.user):
            return Sample.objects.filter(project__lab_people=request.user)
        elif is_bioinfo(request.user):
            return Sample.objects.filter(project__bioinfo_people=request.user)

    # 只能添加自己项目的样本     
    def get_form(self, request, obj=None, **kwargs):
        form = super(SampleAdmin, self).get_form(request, obj, **kwargs)
        if not(request.user.is_superuser or is_manage(request.user)):
            form.base_fields['project'].queryset = Project.objects.filter(lab_people=request.user)
        return form
    

admin.site.register(Sample,SampleAdmin)

