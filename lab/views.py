# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to Singleron.This page is under development.")

# Create your views here.
