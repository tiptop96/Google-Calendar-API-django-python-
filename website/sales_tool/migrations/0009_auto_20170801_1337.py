# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_tool', '0008_auto_20170801_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='internalMeetingCreated',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='event',
            name='researchDone',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='event',
            name='salePointsCreated',
            field=models.NullBooleanField(),
        ),
    ]