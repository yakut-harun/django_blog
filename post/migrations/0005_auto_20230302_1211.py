# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2023-03-02 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Ad Soyad'),
        ),
    ]