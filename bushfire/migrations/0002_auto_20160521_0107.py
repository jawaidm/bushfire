# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='effect',
            name='arrival_area',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='fire_level',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='fire_stopped',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='frb_effect',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='last_burnt',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='waterbomb_effect',
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='coord_type',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Coordinates Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')]),
            preserve_default=True,
        ),
    ]
