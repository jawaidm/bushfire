# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0013_bushfire_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='authorised_by',
            field=models.ForeignKey(verbose_name=b'Authorising Officer', blank=True, to='bushfire.Authorisation', null=True),
            preserve_default=True,
        ),
    ]
