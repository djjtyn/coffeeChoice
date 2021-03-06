# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-24 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_auto_20200324_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intensity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='coffee',
            name='intensity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coffee.Intensity'),
        ),
    ]
