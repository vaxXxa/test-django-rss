# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-02-21 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
