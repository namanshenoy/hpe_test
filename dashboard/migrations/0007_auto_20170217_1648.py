# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20170217_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
