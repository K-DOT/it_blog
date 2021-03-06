# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-03 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0003_auto_20160702_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blognavigation',
            name='nav_items',
        ),
        migrations.AddField(
            model_name='blognavigationitem',
            name='nav',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='navigation.BlogNavigation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blognavigationitem',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
