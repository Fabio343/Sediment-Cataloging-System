# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-20 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='amostra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('tipo', models.CharField(max_length=25)),
                ('descrição', models.TextField(max_length=300, null=True)),
                ('data', models.CharField(max_length=15, null=True)),
                ('granulometria', models.CharField(max_length=15)),
                ('coletador', models.CharField(max_length=50, null=True)),
                ('imagem', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
                ('geologia', models.TextField(max_length=300, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.amostra')),
            ],
        ),
        migrations.CreateModel(
            name='clima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=40, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.amostra')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='continente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
                ('sigla', models.CharField(max_length=15, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.amostra')),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.amostra')),
                ('continente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.continente')),
            ],
        ),
        migrations.CreateModel(
            name='país',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, null=True)),
                ('região', models.CharField(max_length=20, null=True)),
                ('is_destaque', models.BooleanField(default=False)),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.amostra')),
                ('continente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.continente')),
            ],
        ),
        migrations.AddField(
            model_name='estado',
            name='país',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.país'),
        ),
        migrations.AddField(
            model_name='clima',
            name='continente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.continente'),
        ),
        migrations.AddField(
            model_name='clima',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.estado'),
        ),
        migrations.AddField(
            model_name='clima',
            name='país',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.país'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='continente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.continente'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.estado'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='país',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.país'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='amostra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.amostra'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.cidade'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='continente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.continente'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.estado'),
        ),
        migrations.AddField(
            model_name='ambiente',
            name='país',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedimentos.país'),
        ),
    ]