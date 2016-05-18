# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0008_auto_20160517_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='first_attack',
            field=models.ForeignKey(default=1, to='bushfire.FirstAttackAgency'),
            preserve_default=False,
        ),
    ]
