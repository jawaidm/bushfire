# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0003_auto_20160610_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='arson_squad_notified',
            field=models.BooleanField(default=False, verbose_name=b'Arson Squad Notified'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='cause',
            field=models.ForeignKey(default=1, to='bushfire.Cause'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='offence_no',
            field=models.CharField(default=1, max_length=10, verbose_name=b'Offence No.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='prescription',
            field=models.ForeignKey(verbose_name=b'Prescription Burn ID', blank=True, to='bushfire.Prescription', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='source',
            field=models.ForeignKey(verbose_name=b'Reported By', blank=True, to='bushfire.Source', null=True),
            preserve_default=True,
        ),
    ]
