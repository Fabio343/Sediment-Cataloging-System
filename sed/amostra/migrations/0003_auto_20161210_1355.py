# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amostra', '0002_auto_20161210_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='amostra',
            name='ambiente',
        ),
        migrations.AddField(
            model_name='ambiente',
            name='Amostra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostra.Amostra'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='Cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostra.Cidade'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='Estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostra.Estado'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='País',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostra.País'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='continente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amostra.Continente'),
        ),
    ]
