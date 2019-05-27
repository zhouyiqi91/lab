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
    list_display = ('name','p_id','project_type','samples','lab_staff','project_date','bioinfo_staff','metric','view_link')
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

    def yi_xiaji(self, request, queryset):
        queryset.update(xiaji=True)
    yi_xiaji.short_description = "标记为已下机"

    def wei_xiaji(self, request, queryset):
        queryset.update(xiaji=False)
    wei_xiaji.short_description = "标记为未下机"

    def yi_fenxi(self, request, queryset):
        queryset.update(fenxi=True)
    yi_fenxi.short_description = "标记为已分析"

    def wei_fenxi(self, request, queryset):
        queryset.update(fenxi=False)
    wei_fenxi.short_description = "标记为未分析"




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

    list_display = ('name','p_id','sample_date','species','library_type','library_id','xiaji','fenxi','view_link')
    list_filter = ( ('project',RelatedDropdownFilter),
                    ('library_type',ChoiceDropdownFilter),
                    ('sample_date'),
                    ('xiaji'),
                    ('fenxi'),
        )
    search_fields = ['name','sample_date','library_id','description','species','project__p_id','library_type']
    #'created_by__last_name']
    actions = ["export_as_csv","yi_xiaji","wei_xiaji","yi_fenxi","wei_fenxi"]

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

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            created_by = request.user
            name_attr = obj.name.split("\n")
            library_attr = obj.library_id.split("\n")
            library_len = len(library_attr)
            des_attr = obj.description.split("\n")
            des_len = len(des_attr)
            index = 0
            for name_item in name_attr:
                name_item = name_item.strip()
                if name_item:
                    library,des = "",""
                    if library_len > index:
                        library = library_attr[index].strip()
                    if des_len > index:
                        des = des_attr[index].strip()
                    Sample.objects.create(name = name_item,project = obj.project,created_by = created_by,species=obj.species,sample_date = obj.sample_date,description = des,AATI = obj.AATI,report=obj.report,library_id=library,library_type=obj.library_type,xiaji=obj.xiaji,fenxi=obj.fenxi)
                index += 1
        else:
            obj.save()
    

admin.site.register(Sample,SampleAdmin)

