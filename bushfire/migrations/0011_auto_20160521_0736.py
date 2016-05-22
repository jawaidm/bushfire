# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0010_auto_20160521_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='investigation_required',
        ),
        migrations.AddField(
            model_name='detail',
            name='dec',
            field=models.BooleanField(default=False, verbose_name=b'DEC'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='fesa',
            field=models.BooleanField(default=False, verbose_name=b'FESA'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='investigation_req',
            field=models.BooleanField(default=False, verbose_name=b"Invest'n Required"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='lga_bfb',
            field=models.BooleanField(default=False, verbose_name=b'LGA BFB'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='other_force',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='police',
            field=models.BooleanField(default=False, verbose_name=b'POLICE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='ses',
            field=models.BooleanField(default=False, verbose_name=b'SES'),
            preserve_default=True,
        ),
    ]
