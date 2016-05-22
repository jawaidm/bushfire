# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0006_auto_20160521_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='distance',
            field=models.DecimalField(verbose_name=b'Distance (km)', max_digits=6, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='town',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]
