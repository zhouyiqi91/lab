# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class Paper(models.Model):
    name = models.CharField(max_length=80)
    paper_people = models.ManyToManyField(User,related_name="paper_peoples",limit_choices_to=Q(groups__name="paper") )
    paper = models.FileField(upload_to="SGRNJ/Database/test/1.11/lab_project/media/paper/pdf",blank=False)
    date = models.DateField(null=True)
    submit1 = models.FileField(upload_to="SGRNJ/Database/test/1.11/lab_project/media/paper/submit",blank=True)
    submit2 = models.FileField(upload_to="SGRNJ/Database/test/1.11/lab_project/media/paper/submit",blank=True)
    submit1_already = models.BooleanField(verbose_name="submit_1",default=False,editable=False)
    submit2_already = models.BooleanField(verbose_name="submit_2",default=False,editable=False)

    def paper_staff(self):
        return ",".join([p.__str__() for p in self.paper_people.all()])

    def __str__(self):
        return self.name

# Create your models here.
