# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from models import *
from django.db.models import Q
from django.http import HttpResponse
import csv
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
from django.conf.urls import url
from django.template.response import TemplateResponse
#import bulk_admin

def is_manage(user):
    return user.groups.filter(name='manage').exists()

def is_bioinfo(user):
    return user.groups.filter(name='bioinfo').exists()

def is_lab(user):
    return user.groups.filter(name='lab').exists()

class ProjectAdmin(admin.ModelAdmin):
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "输出选中项为csv"

    #exclude = ('project_id',)   
    list_display = ('name','p_id','project_type','samples','lab_staff','project_date','bioinfo_staff','view_link')
    search_fields = ['name','project_type','project_date','description']
    actions = ["export_as_csv"]
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
    #bulk_upload_fields = ()
    def get_urls(self):
        urls = super(SampleAdmin, self).get_urls()
        my_urls = [
            url(r'^my_view/$', self.my_view),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
        )
        if request.method == 'POST':
          for line in request.POST['bulk-create'].split('\n'):
            Sample.objects.create(name=line)
        return TemplateResponse(request, "bulk_create.html", context)
        

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_as_csv.short_description = "输出选中项为csv"

    list_display = ('name','p_id','sample_date','library','xiaji','view_link')
    list_filter = ( ('project',RelatedDropdownFilter),
                    ('sample_date'),
                    ('xiaji'),
        )
    search_fields = ['name','sample_date','library_id','description']
    actions = ["export_as_csv"]

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

