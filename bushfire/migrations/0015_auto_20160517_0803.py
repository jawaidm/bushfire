# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0014_bushfire_authorised_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushfire',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Name/Description'),
            preserve_default=True,
        ),
    ]
