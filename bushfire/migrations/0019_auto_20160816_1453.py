# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0018_auto_20160715_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfire',
            name='other_agency',
        ),
        migrations.AddField(
            model_name='bushfire',
            name='other_final_ctrl',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Other Final Control Agency', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='other_first_attack',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Other First Attack Agency', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='other_hazard_mgt',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Other Hazard Mgt Agency', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='other_initial_ctrl',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Other Initial Control Agency', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='other_cause',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Other Cause', blank=True),
            preserve_default=True,
        ),
    ]
