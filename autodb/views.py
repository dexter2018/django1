# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import DBApplyForm
# Create your views here.

def applydb(request):
    redirect_html = ''
    context = {}
    if request.method != 'POST':
        print ('hello')
        form = DBApplyForm()
        print form.as_p()
        context = {'form': form}
        redirect_html = 'applydb.html'
    else:
        form = DBApplyForm(request.POST)
        if form.is_valid():
            """填写自动创建数据库的相关代码"""
            aform = form.save()
            aform.save()
        else:
            print ('has failed')
        context = {'text': 'hello'}
        redirect_html = 'output.html'

    #print ('hello')
    return render(request, redirect_html,context)