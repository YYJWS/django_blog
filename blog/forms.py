#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django import forms
class Addform(forms.Form):
    a=forms.IntegerField()
    b=forms.IntegerField()
    c=forms.IntegerField()