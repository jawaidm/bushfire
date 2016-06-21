# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0005_auto_20160620_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='arrival_area',
            field=models.DecimalField(default=1, verbose_name=b'Fire Area at Arrival (ha)', max_digits=12, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fire_level',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Final Fire Level', choices=[(1, 1), (2, 2), (3, 3)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fire_stopped',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Fuel Age - Fire Stopped (Yr)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='frb_effect',
            field=models.ForeignKey(verbose_name=b'Presence/Effect of FRB', blank=True, to='bushfire.FrbEffect', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='last_burnt',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Fuel Age - Area Last Burnt (Yr)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='rating',
            field=models.ForeignKey(default=1, verbose_name=b'Area Priority Rating', to='bushfire.PriorityRating'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='waterbomb_effect',
            field=models.ForeignKey(verbose_name=b'Presence/Effect of WaterBomb', blank=True, to='bushfire.WaterBombEffect', null=True),
            preserve_default=True,
        ),
    ]
