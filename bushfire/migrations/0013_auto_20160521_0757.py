# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0012_auto_20160521_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bushfire',
            field=models.OneToOneField(related_name='comments', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='other_agency',
            field=models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='other_cause',
            field=models.CharField(max_length=25, verbose_name=b'Other'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='other_force',
            field=models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True),
            preserve_default=True,
        ),
    ]
