# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autodb', '0002_auto_20170707_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbapplyinfo',
            name='ora_pga',
            field=models.PositiveSmallIntegerField(verbose_name=4),
        ),
        migrations.AlterField(
            model_name='dbapplyinfo',
            name='ora_sga',
            field=models.PositiveSmallIntegerField(verbose_name=4),
        ),
        migrations.AlterField(
            model_name='dbapplyinfo',
            name='os_ip_addr',
            field=models.GenericIPAddressField(),
        ),
    ]
