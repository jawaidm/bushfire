# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0011_auto_20160521_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='first_attack',
            field=models.ForeignKey(to='bushfire.Agency'),
            preserve_default=True,
        ),
    ]
