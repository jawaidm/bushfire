# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bushfire', '0004_auto_20160616_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='assistance_required',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='communications',
            field=models.CharField(default=1, max_length=50, verbose_name=b'Communication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='containment_time',
            field=models.CharField(default=1, max_length=50, verbose_name=b'ET to Contain'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='field_officer',
            field=models.ForeignKey(related_name='init_field_officer', default=1, verbose_name=b'Field Officer', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fire_contained',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='flame_height',
            field=models.DecimalField(default=1, max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='fuel',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='init_authorised_by',
            field=models.ForeignKey(related_name='init_auth_by', verbose_name=b'Authorised By', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='init_authorised_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name=b'Authorised Date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='ops_point',
            field=models.CharField(default=1, max_length=50, verbose_name=b'OPS Point (grid ref)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='ros',
            field=models.CharField(default=1, max_length=50, verbose_name=b'Rate of Spread'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bushfire',
            name='weather',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
