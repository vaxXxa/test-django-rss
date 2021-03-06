# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-02-21 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True)),
                ('published_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='rss.FeedSource'),
        ),
        migrations.AlterUniqueTogether(
            name='feed',
            unique_together=set([('feed_id', 'source')]),
        ),
    ]
