# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):

    type_choice =(
	("RD","研发"),
	("p","项目"),
    )

    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300,blank=True)
    project_type = models.CharField(max_length=2,choices=type_choice)
    project_date = models.DateField()
    people = models.ManyToManyField(User)

    def staff(self):
        return ",".join([str(p) for p in self.people.all()])

    def __str__(self):
        return self.name

class Sample(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300,blank=True)
    project = models.ForeignKey(Project)
    sample_date = models.DateField()
    people = models.ManyToManyField(User)
    AATI = models.ImageField(upload_to="static",blank=True)
    library_id = models.CharField(max_length=30,blank=True)
    report = models.FilePathField(blank=True)

    def library(self):
        if not self.library_id:
            return ""
	else:
            return self.library_id


    def staff(self):
        return ",".join([str(p) for p in self.people.all()])

    def __str__(self):
        return self.name


