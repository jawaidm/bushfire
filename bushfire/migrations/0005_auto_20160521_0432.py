# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0004_auto_20160521_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='origin',
            name='fire_not_found',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='origin',
            name='coord_type',
            field=models.PositiveSmallIntegerField(verbose_name=b'Coordinate Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')]),
            preserve_default=True,
        ),
    ]
