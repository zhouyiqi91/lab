# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import sys
from django.db.models import Q
from django import forms
#from django.core.validators import FileExtensionValidator
reload(sys)
sys.setdefaultencoding('utf-8')


class Project(models.Model):

    def get_user_name(self):
        return self.last_name + self.first_name
    User.__unicode__ = get_user_name


    type_choice =(
	("RD","研发"),
	("P","项目"),
    )

    name = models.CharField(max_length=80)
    project_type = models.CharField(verbose_name="type",max_length=2,choices=type_choice)
    project_date = models.DateField()
    lab_people = models.ManyToManyField(User,related_name="lab_staff",limit_choices_to=Q(groups__name="lab") )
    bioinfo_people = models.ManyToManyField(User,related_name="bioinfo_staff",limit_choices_to=Q(groups__name="bioinfo") )
    description = models.TextField(max_length=300,blank=True)
    p_id = models.CharField(max_length=30,blank=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True)
    root_dir = models.CharField(max_length=255,blank=True)
    report = models.CharField(max_length=255,blank=True)

    def lab_staff(self):
        return ",".join([p.__str__() for p in self.lab_people.all()])

    def bioinfo_staff(self):
        return ",".join([p.__str__() for p in self.bioinfo_people.all()])

    def samples(self):
        number = 0
        samples = self.s_project.all()
        for sample in samples:
            number += 1
        return str(number) 
        
    def view_link(self):
        if self.report:
            return "<a href=/media%s>View</a>" % self.report
        else:
            return ""
    view_link.short_description = 'Report'
    view_link.allow_tags = True

    def metric(self):
        if self.root_dir:
            return "<a href=/media%s/metrics/summary.html target='_blank'>View</a>" % self.root_dir
        else:
            return ""
    metric.allow_tags = True






    def __str__(self):
        return (self.name+" ( "+self.p_id+" )")


class Sample(models.Model):
    #value : display
    library_type_choice = (
    ("scRNA_SCOPE","scRNA_SCOPE"),
    ("scRNA_10X","scRNA_10X"),
    ("RNA_Seq","RNA_Seq"),
    ("WES","WES"),
    ("Methylation","Methylation"),
    )

    species_choice = (
    ("human","human"),
    ("mouse","mouse"),
    ("human_mouse","human_mouse"),
    ("other","other"),
        )

    name = models.TextField()
    project = models.ForeignKey(Project,related_name="s_project")
    species = models.CharField(max_length=20,choices=species_choice)
    sample_date = models.DateField()
    description = models.TextField(blank=True)
    library_id = models.TextField(blank=True)
    library_type = models.CharField(max_length=20,blank=True,choices=library_type_choice)
    AATI = models.ImageField(upload_to="SGRNJ/Database/test/1.11/lab_project/media/AATI",blank=True)
    report = models.CharField(max_length=255,blank=True)
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True)
    xiaji = models.BooleanField(verbose_name="下机",default=False)
    fenxi = models.BooleanField(verbose_name="分析",default=False)


    def lab_staff(self):
        return ",".join([p.__str__() for p in self.project.lab_people.all()])

    def bioinfo_staff(self):
        return ",".join([p.__str__() for p in self.project.bioinfo_people.all()])


    def view_link(self):
        if self.report:
            return "<a href=/media%s>View</a>" % self.report
        else:
            return ""
    view_link.short_description = 'Report'
    view_link.allow_tags = True

    def view_AATI(self):
        if self.AATI:
            return "<a href=/media/%s>View</a>" % self.AATI
        else:
            return ""  

    def p_id(self):
        return self.project.p_id

    def __str__(self):
        return self.name


