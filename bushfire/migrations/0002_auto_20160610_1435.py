# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='initial',
            old_name='date',
            new_name='authorised_date',
        ),
    ]
