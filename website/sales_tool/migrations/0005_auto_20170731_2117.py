# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_tool', '0004_auto_20170731_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uniqueTempKey',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
