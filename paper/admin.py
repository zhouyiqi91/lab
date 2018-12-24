# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from paper.models import *

# Register your models here.
class PaperAdmin(admin.ModelAdmin):
    list_display = ('name','paper_staff','date','submit1_already','submit2_already')
    list_filter = (('date'),)

    def save_model(self, request, obj, form, change):
        obj.submit1_already = False
        obj.submit2_already = False
        if obj.submit1:
            obj.submit1_already = True
        if obj.submit2:
            obj.submit2_already = True
        obj.save()

admin.site.register(Paper,PaperAdmin)
