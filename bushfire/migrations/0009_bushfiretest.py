# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bushfire', '0008_auto_20160630_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='BushfireTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(related_name='bushfire_bushfiretest_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('district', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region', to='bushfire.District', chained_field=b'region', auto_choose=True)),
                ('modifier', models.ForeignKey(related_name='bushfire_bushfiretest_modified', editable=False, to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(to='bushfire.Region')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
