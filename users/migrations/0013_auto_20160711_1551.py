# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-11 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20160710_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
