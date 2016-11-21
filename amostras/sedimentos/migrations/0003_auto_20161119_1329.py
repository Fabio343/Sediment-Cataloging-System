# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-19 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sedimentos', '0002_auto_20161119_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amostra',
            name='UTM',
        ),
        migrations.RemoveField(
            model_name='amostra',
            name='graus',
        ),
        migrations.RemoveField(
            model_name='amostra',
            name='minutos',
        ),
        migrations.RemoveField(
            model_name='amostra',
            name='segundos',
        ),
        migrations.AddField(
            model_name='cidade',
            name='UTM',
            field=models.CharField(default='exit', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='graus',
            field=models.CharField(default='exit', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='minutos',
            field=models.CharField(default='exit', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='segundos',
            field=models.CharField(default='exit', max_length=15),
            preserve_default=False,
        ),
    ]