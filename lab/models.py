# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    project_type = models.CharField(max_length=30)
    project_date = models.DateField()
    people = models.ManyToManyField(User)

    def staff(self):
        return ",".join([str(p) for p in self.people.all()])

    def __str__(self):
        return self.name


