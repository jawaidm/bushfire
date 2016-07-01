# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0007_auto_20160621_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushfire',
            name='cause',
            field=models.ForeignKey(blank=True, to='bushfire.Cause', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='direction',
            field=models.ForeignKey(verbose_name=b'Direction', blank=True, to='bushfire.Direction', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='distance',
            field=models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=6, blank=True, null=True, verbose_name=b'Distance (km)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='incident_no',
            field=models.CharField(max_length=10, verbose_name=b'Fire Incident No.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='lot_no',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Lot Number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='offence_no',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Offence No.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='place',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='prescription',
            field=models.ForeignKey(verbose_name=b'Pres Burn ID', blank=True, to='bushfire.Prescription', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='street',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='town',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='bushfire',
            field=models.ForeignKey(related_name='comments', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
    ]
