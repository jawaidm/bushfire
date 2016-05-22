# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0003_activity_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='bushfire',
            field=models.OneToOneField(related_name='location', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='origin',
            name='bushfire',
            field=models.OneToOneField(related_name='origin', to='bushfire.Bushfire'),
            preserve_default=True,
        ),
    ]
