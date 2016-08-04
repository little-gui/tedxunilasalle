# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.TextField(default='', verbose_name='Sub-titulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='bodytext',
            field=models.TextField(default='', verbose_name='Mensagem'),
        ),
    ]
