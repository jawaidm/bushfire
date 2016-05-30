# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Activity Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AerialForces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.PositiveSmallIntegerField(verbose_name=b'Agency Name', choices=[(1, b'Fixed Wing'), (2, b'Helicopter')])),
                ('observer', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('transporter', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ignition', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('water_bomber', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Agency Name')),
                ('code', models.CharField(max_length=10, verbose_name=b'Agency Short Code')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AreaBurnt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.DecimalField(verbose_name=b'Area (ha)', max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('origin', models.BooleanField(default=False, verbose_name=b'Point of Origin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttendingOrganisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('other', models.CharField(max_length=25, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Authorisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('auth_type', models.PositiveSmallIntegerField(choices=[(1, b'Initial'), (2, b'Final')])),
                ('creator', models.ForeignKey(related_name='bushfire_authorisation_created', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_type', models.PositiveSmallIntegerField(choices=[(1, b'Initial'), (2, b'Final')])),
                ('area', models.DecimalField(verbose_name=b'Area (ha)', max_digits=12, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('other_agency', models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True)),
                ('dec', models.BooleanField(default=False, verbose_name=b'DEC')),
                ('lga_bfb', models.BooleanField(default=False, verbose_name=b'LGA BFB')),
                ('fesa', models.BooleanField(default=False, verbose_name=b'FESA')),
                ('ses', models.BooleanField(default=False, verbose_name=b'SES')),
                ('police', models.BooleanField(default=False, verbose_name=b'POLICE')),
                ('other_force', models.CharField(max_length=25, null=True, verbose_name=b'Other', blank=True)),
                ('known_possible', models.PositiveSmallIntegerField(verbose_name=b'Known/Possible', choices=[(1, b'Known'), (2, b'Possible')])),
                ('other_cause', models.CharField(max_length=25, verbose_name=b'Other')),
                ('investigation_req', models.BooleanField(default=False, verbose_name=b"Invest'n Required")),
                ('cause', models.ForeignKey(to='bushfire.Cause')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('code', models.CharField(max_length=3)),
                ('archive_date', models.DateField(help_text=b'Archive this District (prevent from creating new ePFPs)', null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinalBushfire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Name/Description')),
                ('incident_no', models.CharField(max_length=10, verbose_name=b'Incident No.')),
                ('season', models.CharField(max_length=9)),
                ('dfes_incident_no', models.CharField(max_length=10, verbose_name=b'DFES Incident No.')),
                ('job_code', models.CharField(max_length=10, verbose_name=b'Job Code')),
                ('potential_fire_level', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
                ('coord_type', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Coordinates Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')])),
                ('lat_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Decimal)')),
                ('lat_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Degrees)')),
                ('lat_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Minutes)')),
                ('lon_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Decimal)')),
                ('lon_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Degrees)')),
                ('lon_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Minutes)')),
                ('mga_zone', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Zone')),
                ('mga_easting', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Easting')),
                ('mga_northing', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Northing')),
                ('fd_letter', models.CharField(max_length=2, null=True, verbose_name=b'FD Letter', blank=True)),
                ('fd_number', models.PositiveSmallIntegerField(null=True, verbose_name=b'FD Number', blank=True)),
                ('fd_tenths', models.CharField(max_length=2, null=True, verbose_name=b'FD Tenths', blank=True)),
                ('creator', models.ForeignKey(related_name='bushfire_finalbushfire_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(to='bushfire.District')),
                ('modifier', models.ForeignKey(related_name='bushfire_finalbushfire_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FireBehaviour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name=b'Name/Description')),
                ('fuel_weight', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('fdi', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ros', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('bushfire', models.ForeignKey(related_name='fire_behaviour', to='bushfire.FinalBushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FirstAttackAgency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bushfire', models.ForeignKey(related_name='first_attack', to='bushfire.FinalBushfire')),
                ('final_control', models.ForeignKey(related_name='final_control', verbose_name=b'Final Controlling Agency', blank=True, to='bushfire.Agency', null=True)),
                ('first_attack', models.ForeignKey(related_name='first_attack', verbose_name=b'First Attack Agency', blank=True, to='bushfire.Agency', null=True)),
                ('hazard_mgt', models.ForeignKey(related_name='hazard_mgt', verbose_name=b'Hazard Management Agency', blank=True, to='bushfire.Agency', null=True)),
                ('initial_control', models.ForeignKey(related_name='initial_control', verbose_name=b'Initial Controlling Agency', blank=True, to='bushfire.Agency', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrbEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroundForces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.PositiveSmallIntegerField(verbose_name=b'Agency Name', choices=[(1, b'Initial DEC Dispatch'), (2, b'DEC Peak'), (3, b'Other Agencies Peak')])),
                ('persons', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('pumpers', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('plant', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('bushfire', models.ForeignKey(related_name='ground_forces', to='bushfire.FinalBushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitialActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitialActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Activity Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitialBushfire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Name/Description')),
                ('incident_no', models.CharField(max_length=10, verbose_name=b'Incident No.')),
                ('season', models.CharField(max_length=9)),
                ('dfes_incident_no', models.CharField(max_length=10, verbose_name=b'DFES Incident No.')),
                ('job_code', models.CharField(max_length=10, verbose_name=b'Job Code')),
                ('potential_fire_level', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
                ('coord_type', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Coordinates Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')])),
                ('lat_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Decimal)')),
                ('lat_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Degrees)')),
                ('lat_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Minutes)')),
                ('lon_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Decimal)')),
                ('lon_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Degrees)')),
                ('lon_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Minutes)')),
                ('mga_zone', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Zone')),
                ('mga_easting', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Easting')),
                ('mga_northing', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Northing')),
                ('fd_letter', models.CharField(max_length=2, null=True, verbose_name=b'FD Letter', blank=True)),
                ('fd_number', models.PositiveSmallIntegerField(null=True, verbose_name=b'FD Number', blank=True)),
                ('fd_tenths', models.CharField(max_length=2, null=True, verbose_name=b'FD Tenths', blank=True)),
                ('creator', models.ForeignKey(related_name='bushfire_initialbushfire_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(to='bushfire.District')),
                ('modifier', models.ForeignKey(related_name='bushfire_initialbushfire_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitialComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('fuel', models.CharField(max_length=50)),
                ('ros', models.CharField(max_length=50, verbose_name=b'Rate of Spread')),
                ('flame_height', models.DecimalField(max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('assistance_required', models.CharField(max_length=50)),
                ('fire_contained', models.BooleanField(default=False)),
                ('containment_time', models.CharField(max_length=50, verbose_name=b'ET to Contain')),
                ('ops_point', models.CharField(max_length=50, verbose_name=b'OPS Point (grid ref)')),
                ('communications', models.CharField(max_length=50)),
                ('weather', models.CharField(max_length=50)),
                ('bushfire', models.OneToOneField(related_name='initial_comments', to='bushfire.InitialBushfire')),
                ('creator', models.ForeignKey(related_name='bushfire_initialcomment_created', editable=False, to=settings.AUTH_USER_MODEL)),
                ('field_officer', models.ForeignKey(verbose_name=b'Field Officer', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(related_name='bushfire_initialcomment_modified', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvestigationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Investigation Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protection', models.PositiveSmallIntegerField(verbose_name=b'Community Protection (%)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('cost', models.DecimalField(verbose_name=b'Est. Cost of Damages ($)', max_digits=12, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('restricted_period', models.BooleanField(default=False)),
                ('prohibited_period', models.BooleanField(default=False)),
                ('inv_undertaken', models.ForeignKey(verbose_name=b'Investigation Undertaken', to='bushfire.InvestigationType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LegalResultType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Legal Result Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_type', models.PositiveSmallIntegerField(choices=[(1, b'Initial'), (2, b'Final')])),
                ('distance', models.DecimalField(verbose_name=b'Distance (km)', max_digits=6, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('place', models.CharField(max_length=25)),
                ('lot_no', models.CharField(max_length=10, verbose_name=b'Lot Number')),
                ('street', models.CharField(max_length=25)),
                ('town', models.CharField(max_length=25)),
                ('direction', models.ForeignKey(verbose_name=b'Direction', to='bushfire.Direction')),
                ('final_bushfire', models.OneToOneField(related_name='final_location', to='bushfire.FinalBushfire')),
                ('initial_bushfire', models.OneToOneField(related_name='initial_location', to='bushfire.InitialBushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Organisation')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_type', models.PositiveSmallIntegerField(choices=[(1, b'Initial'), (2, b'Final')])),
                ('coord_type', models.PositiveSmallIntegerField(verbose_name=b'Coordinate Type', choices=[(1, b'MGA'), (2, b'Lat/Long'), (3, b'FD Grid')])),
                ('fire_not_found', models.BooleanField(default=False)),
                ('lat_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Decimal)')),
                ('lat_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Degrees)')),
                ('lat_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Latitude (Minutes)')),
                ('lon_decimal', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Decimal)')),
                ('lon_degrees', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Degrees)')),
                ('lon_minutes', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'Longitude (Minutes)')),
                ('mga_zone', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Zone')),
                ('mga_easting', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Easting')),
                ('mga_northing', models.DecimalField(decimal_places=1, validators=[django.core.validators.MinValueValidator(0)], max_digits=12, blank=True, null=True, verbose_name=b'MGA Northing')),
                ('fd_letter', models.CharField(max_length=2, null=True, verbose_name=b'FD Letter', blank=True)),
                ('fd_number', models.PositiveSmallIntegerField(null=True, verbose_name=b'FD Number', blank=True)),
                ('fd_tenths', models.CharField(max_length=2, null=True, verbose_name=b'FD Tenths', blank=True)),
                ('final_bushfire', models.OneToOneField(related_name='final_origin', to='bushfire.FinalBushfire')),
                ('initial_bushfire', models.OneToOneField(related_name='initial_origin', to='bushfire.InitialBushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('burn_id', models.CharField(max_length=7)),
            ],
            options={
                'ordering': ['burn_id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriorityRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrivateDamage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('bushfire', models.ForeignKey(related_name='private_damages', to='bushfire.FinalBushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrivateDamageType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Private Damage Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicDamage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.DecimalField(verbose_name=b'Area (ha)', max_digits=12, decimal_places=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('bushfire', models.ForeignKey(related_name='public_damages', to='bushfire.FinalBushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicDamageType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Public Damage Type')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arson_squad_notified', models.BooleanField(default=False, verbose_name=b'Arson Squad Notified')),
                ('offence_no', models.TextField(verbose_name=b'Offence No.')),
                ('bushfire', models.ForeignKey(related_name='reporting', to='bushfire.FinalBushfire')),
                ('cause', models.ForeignKey(to='bushfire.Cause')),
                ('prescription', models.ForeignKey(verbose_name=b'Prescription Burn ID', blank=True, to='bushfire.Prescription', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bushfire', models.ForeignKey(related_name='responses', to='bushfire.FinalBushfire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Agency Name')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tenure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WaterBombEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='response',
            name='response',
            field=models.ForeignKey(to='bushfire.ResponseType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set([('bushfire', 'response')]),
        ),
        migrations.AddField(
            model_name='reporter',
            name='source',
            field=models.ForeignKey(verbose_name=b'Reported By', blank=True, to='bushfire.Source', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicdamage',
            name='damage_type',
            field=models.ForeignKey(to='bushfire.PublicDamageType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicdamage',
            name='fuel_type',
            field=models.ForeignKey(to='bushfire.FuelType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='publicdamage',
            unique_together=set([('bushfire', 'damage_type', 'fuel_type')]),
        ),
        migrations.AddField(
            model_name='privatedamage',
            name='damage_type',
            field=models.ForeignKey(to='bushfire.PrivateDamageType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='privatedamage',
            unique_together=set([('bushfire', 'damage_type')]),
        ),
        migrations.AddField(
            model_name='legal',
            name='legal_result',
            field=models.ForeignKey(to='bushfire.LegalResultType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='initialbushfire',
            name='region',
            field=models.ForeignKey(to='bushfire.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='initialactivity',
            name='activity',
            field=models.ForeignKey(to='bushfire.InitialActivityType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='initialactivity',
            name='bushfire',
            field=models.ForeignKey(related_name='initial_activities', to='bushfire.InitialBushfire'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='initialactivity',
            unique_together=set([('bushfire', 'activity')]),
        ),
        migrations.AlterUniqueTogether(
            name='groundforces',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='firebehaviour',
            name='fuel_type',
            field=models.ForeignKey(related_name='fuel_types_fire', blank=True, to='bushfire.FuelType', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='firebehaviour',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='finalbushfire',
            name='region',
            field=models.ForeignKey(to='bushfire.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effect',
            name='bushfire',
            field=models.ForeignKey(related_name='effect', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(to='bushfire.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='final_bushfire',
            field=models.OneToOneField(related_name='final_detail', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='first_attack',
            field=models.ForeignKey(to='bushfire.Agency'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='fuel_type',
            field=models.ForeignKey(to='bushfire.FuelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='initial_bushfire',
            field=models.OneToOneField(related_name='initial_detail', to='bushfire.InitialBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='tenure',
            field=models.ForeignKey(to='bushfire.Tenure'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='bushfire',
            field=models.ForeignKey(related_name='final_comments', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(related_name='bushfire_comment_created', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='modifier',
            field=models.ForeignKey(related_name='bushfire_comment_modified', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorisation',
            name='final_bushfire',
            field=models.OneToOneField(related_name='final_authorisation', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorisation',
            name='initial_bushfire',
            field=models.OneToOneField(related_name='initial_authorisation', to='bushfire.InitialBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorisation',
            name='modifier',
            field=models.ForeignKey(related_name='bushfire_authorisation_modified', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorisation',
            name='name',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendingorganisation',
            name='bushfire',
            field=models.ForeignKey(related_name='attending_organisations', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendingorganisation',
            name='name',
            field=models.ForeignKey(to='bushfire.Organisation'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attendingorganisation',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='areaburnt',
            name='bushfire',
            field=models.ForeignKey(related_name='areas_burnt', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaburnt',
            name='fuel_type',
            field=models.ForeignKey(related_name='fuel_types', to='bushfire.FuelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaburnt',
            name='tenure',
            field=models.ForeignKey(related_name='tenures', to='bushfire.Tenure'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='areaburnt',
            unique_together=set([('bushfire', 'tenure', 'fuel_type')]),
        ),
        migrations.AddField(
            model_name='aerialforces',
            name='bushfire',
            field=models.ForeignKey(related_name='aerial_forces', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='aerialforces',
            unique_together=set([('bushfire', 'name')]),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity',
            field=models.ForeignKey(to='bushfire.ActivityType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='bushfire',
            field=models.ForeignKey(related_name='activities', to='bushfire.FinalBushfire'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='activity',
            unique_together=set([('bushfire', 'activity')]),
        ),
    ]
