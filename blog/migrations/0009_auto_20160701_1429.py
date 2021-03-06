# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160701_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNavigationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_url', models.URLField()),
                ('page', models.ManyToManyField(to='blog.BlogFlatPage')),
                ('post', models.ManyToManyField(to='blog.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='blognavigation',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blognavigation',
            name='post',
        ),
        migrations.AddField(
            model_name='blognavigation',
            name='item',
            field=models.ManyToManyField(to='blog.BlogNavigationItem'),
        ),
    ]
