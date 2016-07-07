# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0015_auto_20160705_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushfire',
            name='arrival_area',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Fire Area at Arrival (ha)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='assistance_required',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='communications',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Communication', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='containment_time',
            field=models.CharField(max_length=50, null=True, verbose_name=b'ET to Contain', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='coord_type',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Coordinate Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='fire_level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Final Fire Level', choices=[(1, 1), (2, 2), (3, 3)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='flame_height',
            field=models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='fuel',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='ops_point',
            field=models.CharField(max_length=50, null=True, verbose_name=b'OPS Point (grid ref)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='other_agency',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Other Agency', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='rating',
            field=models.ForeignKey(verbose_name=b'Area Priority Rating', blank=True, to='bushfire.PriorityRating', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='ros',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Rate of Spread', blank=True),
            preserve_default=True,
        ),
    ]
