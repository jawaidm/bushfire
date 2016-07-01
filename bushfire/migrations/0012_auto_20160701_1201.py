# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0011_bushfire_other_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='investigation_req',
            field=models.BooleanField(default=False, verbose_name=b"Invest'n Required"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='known_possible',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Known/Possible', choices=[(1, b'Known'), (2, b'Possible')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='other_cause',
            field=models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='cause',
            field=models.ForeignKey(default=1, to='bushfire.Cause'),
            preserve_default=False,
        ),
    ]
