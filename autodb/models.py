# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm

# Create your models here.
class DBApplyInfo(models.Model):
    """自动创建数据库申请单"""
    os_username = models.CharField(max_length=20, default='oracle')
    os_passwd = models.CharField(max_length=20, default='oracle123')
    os_ip_addr = models.GenericIPAddressField()
    ora_home = models.CharField(max_length=100, default='/u01/app/oracle/product/11.2.0/dbhome_1')
    ora_sid = models.CharField(max_length=8)
    ora_passwd = models.CharField(max_length=20, default='oracle123')
    ora_charset = models.CharField(max_length=15)
    ora_ncharset = models.CharField(max_length=15)
    ora_sga = models.PositiveSmallIntegerField()
    ora_pga = models.PositiveSmallIntegerField()
    #text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class DBApplyForm(ModelForm):
    class Meta:
        model = DBApplyInfo
        fields = ['os_ip_addr', 'ora_sid', 'ora_charset', 'ora_ncharset', 'ora_sga', 'ora_pga']