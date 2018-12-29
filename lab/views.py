# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from lab.models import Project,Sample

def welcome(request):    
    return HttpResponse("Welcome to Singleron.This page is under development.")

def display(request):
    projects = Project.objects.all()
    return render(request,'lab/display.html',{'projects':projects})

def sample_lists(request,project_uid):
    project = Project.objects.get(id=project_uid)
    samples = Sample.objects.filter(project__id=project_uid)
    """
    for sample in samples:
        sampleProject.samples(sample)
    """
    return render(request,'lab/sample_lists.html',{'samples':samples,'project':project})

# Create your views here.
