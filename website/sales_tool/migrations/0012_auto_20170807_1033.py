# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_tool', '0011_auto_20170807_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
