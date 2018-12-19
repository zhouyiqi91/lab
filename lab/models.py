# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import sys
from django.db.models import Q
#from django.core.validators import FileExtensionValidator
reload(sys)
sys.setdefaultencoding('utf-8')

class Employee(models.Model):
    type_choice =(
    ("lab","实验"),
    ("bioinfo","生信"),
    ("xingzheng","行政"),
    ("manage","管理"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(verbose_name="部门",max_length=30,choices=type_choice)

    def get_user_name(self):
        return self.last_name + self.first_name

    User.__unicode__ = get_user_name

    def __str__(self):
        return(self.user.__unicode__())

"""
class Lab_staff(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,limit_choices_to={'department': "lab"},)

    def __str__(self):
        #return(self.employee.__str__())
        return("yes")

class Bioinfo_staff(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    #,limit_choices_to={'department': "bioinfo"},)

    def __str__(self):
        return ("yes")
        #return(self.employee.__str__())
"""


class Project(models.Model):

    type_choice =(
	("RD","研发"),
	("p","项目"),
    )

    name = models.CharField(max_length=30)
    project_type = models.CharField(max_length=2,choices=type_choice)
    project_date = models.DateField()
    people = models.ManyToManyField(Employee,limit_choices_to=Q(department="lab") | Q(department="bioinfo") )
    description = models.TextField(max_length=300,blank=True)

    def staff(self):
        return ",".join([p.__str__() for p in self.people.all()])


    def __str__(self):
        return self.name


class Sample(models.Model):
    library_type_choice = (
    ("scope","scRNA-SCOPE"),
    ("X10","scRNA-10X"),
    ("RNA","RNA-Seq"),
    ("WES","WES"),
    )

    species_choice = (
    ("human","hm"),
    ("mouse","mm"),
    ("human_mouse","hm_mm"),
    ("other","other"),
        )

    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project)
    species = models.CharField(max_length=20,choices=species_choice)
    sample_date = models.DateField()
    #people= models.ManyToManyField(Employee,limit_choices_to=Q(department="lab") | Q(department="bioinfo") )
    description = models.TextField(max_length=300,blank=True)
    library_id = models.CharField(max_length=30,blank=True)
    library_type = models.CharField(max_length=20,blank=True,choices=library_type_choice)
    AATI = models.ImageField(upload_to="AATI",blank=True)
    report = models.CharField(max_length=255,blank=True)

    def library(self):
        if not self.library_id:
            return ""
	else:
            return self.library_id


    def staff(self):
        #return ",".join([p for p in self.people.__str__()])
        return ",".join([p.__str__() for p in self.project.people.all()])

    def view_link(self):
        if self.report:
            return "<a href=/media/report/%s>View</a>" % self.report
        else:
            return ""
    view_link.short_description = 'Report'
    view_link.allow_tags = True

    def __str__(self):
        return self.name


