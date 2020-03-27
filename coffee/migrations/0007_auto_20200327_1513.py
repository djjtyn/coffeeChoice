# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-27 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0006_coffee_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='User', max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AddField(
            model_name='comment',
            name='Coffee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='coffee.Coffee'),
        ),
    ]
