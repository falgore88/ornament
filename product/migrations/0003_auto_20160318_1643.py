# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 16:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160318_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_type',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Product_type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 18, 16, 43, 8, 711631, tzinfo=utc)),
        ),
    ]