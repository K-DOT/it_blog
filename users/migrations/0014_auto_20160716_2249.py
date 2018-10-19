# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-16 18:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20160711_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Խումբ', 'verbose_name_plural': 'Խմբեր'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Օգտագործող', 'verbose_name_plural': 'Օգտագործողներ'},
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ավատար'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_posts',
            field=models.ManyToManyField(blank=True, related_name='favorite', to='blog.Post', verbose_name='Սիրված գրառումներ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='personal_info',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Անձնական ինֆորմացիա'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True, verbose_name='Կայք'),
        ),
    ]
