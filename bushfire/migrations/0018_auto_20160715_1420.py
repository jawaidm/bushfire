# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0017_auto_20160705_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendingorganisation',
            name='name',
            field=models.ForeignKey(default=1, to='bushfire.Organisation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='cause',
            field=models.ForeignKey(blank=True, to='bushfire.Cause', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='dfes_incident_no',
            field=models.CharField(max_length=10, null=True, verbose_name=b'DFES Incident No.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='field_officer',
            field=models.ForeignKey(related_name='init_field_officer', verbose_name=b'Field Officer', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='first_attack',
            field=models.ForeignKey(related_name='first_attack', verbose_name=b'First Attack Agency', blank=True, to='bushfire.Agency', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='known_possible',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Known/Possible', choices=[(1, b'Known'), (2, b'Possible')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='potential_fire_level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 1), (2, 2), (3, 3)]),
            preserve_default=True,
        ),
    ]
