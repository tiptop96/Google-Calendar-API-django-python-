# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_tool', '0006_auto_20170731_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='saleDocLink',
            field=models.URLField(null=True),
        ),
    ]
