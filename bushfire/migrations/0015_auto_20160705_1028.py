# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bushfire', '0014_bushfiretest2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('activity', models.ForeignKey(to='bushfire.ActivityType')),
                ('bushfire', models.ForeignKey(related_name='activities2', to='bushfire.BushfireTest2')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='activity2',
            unique_together=set([('bushfire', 'activity')]),
        ),
    ]
