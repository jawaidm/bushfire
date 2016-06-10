# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0002_auto_20160610_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='coord_type',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Coordinate Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fd_letter',
            field=models.CharField(max_length=2, null=True, verbose_name=b'FD Letter', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fd_number',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'FD Number', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fd_tenths',
            field=models.CharField(max_length=2, null=True, verbose_name=b'FD Tenths', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fire_not_found',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='lat_decimal',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Decimal)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='lat_degrees',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Degrees)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='lat_minutes',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='lon_decimal',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Decimal)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='lon_degrees',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Degrees)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='lon_minutes',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='mga_easting',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Easting'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='mga_northing',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Northing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='mga_zone',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Zone'),
            preserve_default=True,
        ),
    ]
