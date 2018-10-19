# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-25 18:28
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160625_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gplus',
            field=models.URLField(blank=True, validators=[users.models.URLDomainValidator(['plus.google.com'])], verbose_name='Google Plus'),
        ),
    ]
