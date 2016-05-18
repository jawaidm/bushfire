# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0005_remove_bushfire_potential_fire_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='details',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='first_attack',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='location',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='origin',
        ),
        migrations.AddField(
            model_name='bushfire',
            name='potential_fire_level',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3)]),
            preserve_default=False,
        ),
    ]
