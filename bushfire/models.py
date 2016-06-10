from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
#from pbs.prescription.models import (Prescription, Region, District)
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator
#from smart_selects.db_fields import ChainedForeignKey
from bushfire.base import Audit
from django.core.exceptions import (ValidationError)

import sys
#sys.path.append('/root/project1')
#from appx.models import Foox
#sys.path.append('/home/jawaidm/projects/pbs')
#from pbs.prescription.models import (Prescription, Region, District, Tenure, FuelType)


FIRE_LEVEL_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
)

AUTH_TYPE_CHOICES = (
    (1, 'Initial'),
    (2, 'Final'),
)

#class Audit(models.Model):
#    creator = models.ForeignKey(User, related_name='creator')
#    modifier = models.ForeignKey(User, related_name='modifier')
#    created = models.DateTimeField(default=timezone.now, editable=False)
#    modified = models.DateTimeField(auto_now=True, editable=False)

@python_2_unicode_compatible
class Prescription(models.Model):
    burn_id = models.CharField(max_length=7)

    class Meta:
        ordering = ['burn_id']

    def __str__(self):
        return self.burn_id


@python_2_unicode_compatible
class Region(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class District(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=3)
    archive_date = models.DateField(
        null=True, blank=True, help_text="Archive this District (prevent from creating new ePFPs)"
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tenure(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class FuelType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class _InitialBushfire(Audit):
    COORD_TYPE_1 = 1
    COORD_TYPE_2 = 2
    COORD_TYPE_3 = 3
    COORD_TYPE_CHOICES = (
        (COORD_TYPE_1, 'MGA'),
        (COORD_TYPE_2, 'Lat/Long'),
        (COORD_TYPE_3, 'FD Grid'),
    )


    # Main Area
    region = models.ForeignKey(Region)
#    district = models.ForeignKey(District)
    district = ChainedForeignKey(
        District, chained_field="region", chained_model_field="region",
        show_all=False, auto_choose=True)

    name = models.CharField(max_length=100, verbose_name="Name/Description")
    incident_no = models.CharField(verbose_name="Incident No.", max_length=10)
    season = models.CharField(max_length=9)
    dfes_incident_no = models.CharField(verbose_name="DFES Incident No.", max_length=10)
    job_code = models.CharField(verbose_name="Job Code", max_length=10, null=True, blank=True)
    potential_fire_level = models.PositiveSmallIntegerField(choices=FIRE_LEVEL_CHOICES)

    #authorised_by = models.ForeignKey('Authorisation', verbose_name="Authorising Officer", blank=True, null=True)
    #reporting = models.ForeignKey('Reporter', verbose_name="Reporting and  Cause")


    # TABS

    # Point of Origin
    #   location = models.ForeignKey('Location')
    #   origin = models.ForeignKey('Origin')
    #   TODO number of dp
    coord_type = models.PositiveSmallIntegerField(choices=COORD_TYPE_CHOICES, verbose_name="Coordinates Type", null=True, blank=True)
    lat_decimal = models.DecimalField(verbose_name="Latitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lat_degrees = models.DecimalField(verbose_name="Latitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lat_minutes = models.DecimalField(verbose_name="Latitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_decimal = models.DecimalField(verbose_name="Longitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_degrees = models.DecimalField(verbose_name="Longitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_minutes = models.DecimalField(verbose_name="Longitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)

    mga_zone = models.DecimalField(verbose_name="MGA Zone", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    mga_easting = models.DecimalField(verbose_name="MGA Easting", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    mga_northing = models.DecimalField(verbose_name="MGA Northing", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)

    fd_letter = models.CharField(verbose_name="FD Letter", max_length=2, null=True, blank=True)
    fd_number = models.PositiveSmallIntegerField(verbose_name="FD Number", null=True, blank=True)
    fd_tenths = models.CharField(verbose_name="FD Tenths", max_length=2, null=True, blank=True)

    class Meta:
        abstract = True


class BushfireBase(Audit):
    region = models.ForeignKey(Region)
#    district = models.ForeignKey(District)
    district = ChainedForeignKey(
        District, chained_field="region", chained_model_field="region",
        show_all=False, auto_choose=True)

    name = models.CharField(max_length=100, verbose_name="Fire Name")
    incident_no = models.CharField(verbose_name="Incident No.", max_length=10)
    season = models.CharField(max_length=9)
    dfes_incident_no = models.CharField(verbose_name="DFES Incident No.", max_length=10)
    job_code = models.CharField(verbose_name="Job Code", max_length=10, null=True, blank=True)
    potential_fire_level = models.PositiveSmallIntegerField(choices=FIRE_LEVEL_CHOICES)

    authorised_by = models.ForeignKey(User, verbose_name="Authorised By", blank=True, null=True)
    authorised_date = models.DateTimeField(verbose_name='Authorised Date', default=timezone.now, null=True, blank=True)

    # Origin
    COORD_TYPE_1 = 1
    COORD_TYPE_2 = 2
    COORD_TYPE_3 = 3
    COORD_TYPE_CHOICES = (
        (COORD_TYPE_1, 'MGA'),
        (COORD_TYPE_2, 'Lat/Long'),
        (COORD_TYPE_3, 'FD Grid'),
    )

    coord_type = models.PositiveSmallIntegerField(choices=COORD_TYPE_CHOICES, verbose_name="Coordinate Type")
    fire_not_found = models.BooleanField(default=False)
    # TODO number of dp
    lat_decimal = models.DecimalField(verbose_name="Latitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lat_degrees = models.DecimalField(verbose_name="Latitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lat_minutes = models.DecimalField(verbose_name="Latitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_decimal = models.DecimalField(verbose_name="Longitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_degrees = models.DecimalField(verbose_name="Longitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_minutes = models.DecimalField(verbose_name="Longitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)

    mga_zone = models.DecimalField(verbose_name="MGA Zone", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    mga_easting = models.DecimalField(verbose_name="MGA Easting", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    mga_northing = models.DecimalField(verbose_name="MGA Northing", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)

    fd_letter = models.CharField(verbose_name="FD Letter", max_length=2, null=True, blank=True)
    fd_number = models.PositiveSmallIntegerField(verbose_name="FD Number", null=True, blank=True)
    fd_tenths = models.CharField(verbose_name="FD Tenths", max_length=2, null=True, blank=True)


    # Location
    distance = models.DecimalField(
        verbose_name="Distance (km)", max_digits=6, decimal_places=1,
        validators=[MinValueValidator(0)])
    direction = models.ForeignKey('Direction', verbose_name="Direction")
    place = models.CharField(max_length=25)
    lot_no = models.CharField(verbose_name="Lot Number", max_length=10)
    street = models.CharField(max_length=25)
    town = models.CharField(max_length=25)

    #reporting = models.ForeignKey('Reporter', verbose_name="Reporting and  Cause")


    # TABS

    # Point of Origin
    #   location = models.ForeignKey('Location')
    #   origin = models.ForeignKey('Origin')
    #   TODO number of dp
#    coord_type = models.PositiveSmallIntegerField(choices=COORD_TYPE_CHOICES, verbose_name="Coordinates Type", null=True, blank=True)
#    lat_decimal = models.DecimalField(verbose_name="Latitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lat_degrees = models.DecimalField(verbose_name="Latitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lat_minutes = models.DecimalField(verbose_name="Latitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lon_decimal = models.DecimalField(verbose_name="Longitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lon_degrees = models.DecimalField(verbose_name="Longitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lon_minutes = models.DecimalField(verbose_name="Longitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#
#    mga_zone = models.DecimalField(verbose_name="MGA Zone", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    mga_easting = models.DecimalField(verbose_name="MGA Easting", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    mga_northing = models.DecimalField(verbose_name="MGA Northing", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#
#    fd_letter = models.CharField(verbose_name="FD Letter", max_length=2, null=True, blank=True)
#    fd_number = models.PositiveSmallIntegerField(verbose_name="FD Number", null=True, blank=True)
#    fd_tenths = models.CharField(verbose_name="FD Tenths", max_length=2, null=True, blank=True)

    # Effects/Agencies
    #   effect = models.ForeignKey('Effect')
    #   first_attack = models.ForeignKey('FirstAttackAgency')
    #   Response goes with this section
#    frb_effect = models.ForeignKey('FrbEffect', null=True, blank=True)
    #fire_stopped = models.PositiveSmallIntegerField(verbose_name="Fuel Age - Fire Stopped (Yr)", null=True, blank=True)
    #waterbomb_effect = models.ForeignKey('WaterBombEffect', null=True, blank=True)
    #last_burnt = models.PositiveSmallIntegerField(verbose_name="Fuel Age - Area Last Burnt (Yr)", null=True, blank=True)
    #arrival_area = models.DecimalField(verbose_name="Fire Area at Arrival (ha)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)])
    #fire_level = models.PositiveSmallIntegerField(choices=FIRE_LEVEL_CHOICES)
    #rating = models.ForeignKey('PriorityRating', null=True, blank=True, verbose_name="Area Priority Rating")

    #first_attack = models.ForeignKey('Agency', verbose_name="First Attack Agency", null=True, blank=True, related_name='first_attack')
    #hazard_mgt = models.ForeignKey('Agency', verbose_name="Hazard Management Agency", null=True, blank=True, related_name='hazard_mgt')
    #initial_control = models.ForeignKey('Agency', verbose_name="Initial Controlling Agency", null=True, blank=True, related_name='initial_control')
    #final_control = models.ForeignKey('Agency', verbose_name="Final Controlling Agency", null=True, blank=True, related_name='final_control')

#    response = models.ForeignKey('ResponseType')

    # Effects/Agencies
    #   AreaBurnt goes with this section
    #   GroundForces goes with this section
    #   AerialForces goes with this section
#    tenure = models.ForeignKey('Tenure', related_name='tenures')
    #fuel_type = models.ForeignKey('FuelType', related_name='fuel_types') # vegetation_type was renamed to fuel_type in PBS
    #area = models.DecimalField(verbose_name="Area (ha)", max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
#    origin = models.BooleanField(verbose_name="Point of Origin", default=False)


    # Attendance/Behaviour
    #   FireBehaviour goes with this section
    #   AttendingOrganisation goes with this section

    # Damages/Legal
    #   Legal goes with this section
    #   PublicDamage goes with this section
    #   PrivateDamage goes with this section

    # Comments
    #   FinalComment goes with this section

    # Details (Initial)
    #details = models.ForeignKey('Detail')

    # Comments (Initial)
    #comments = models.ForeignKey('Comment')

    def user_unicode_patch(self):
        """ overwrite the User model's __unicode__() method """
        if self.first_name or self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        return self.username
    User.__unicode__ = user_unicode_patch

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


#@python_2_unicode_compatible
#class InitialBushfire(BushfireBase):
#    pass
#    #name = models.CharField(max_length=100, verbose_name="Name/Description")
#
#    def __str__(self):
#        return self.name


@python_2_unicode_compatible
class Bushfire(BushfireBase):
    pass
    #name = models.CharField(max_length=100, verbose_name="Name/Description")

    class Meta:
        unique_together = ('district', 'incident_no', 'season')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Location2(models.Model):
    distance = models.DecimalField(
        verbose_name="Distance (km)", max_digits=6, decimal_places=1,
        validators=[MinValueValidator(0)])
    direction = models.ForeignKey('Direction', verbose_name="Direction")
    place = models.CharField(max_length=25)
    lot_no = models.CharField(verbose_name="Lot Number", max_length=10)
    street = models.CharField(max_length=25)
    town = models.CharField(max_length=25)
    #bushfire = models.OneToOneField(Bushfire, related_name='location')

    def __str__(self):
        return self.direction.name



@python_2_unicode_compatible
class Source(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Cause(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Direction(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=3)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class FrbEffect(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class WaterBombEffect(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PriorityRating(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Agency(models.Model):

    name = models.CharField(max_length=50, verbose_name="Agency Name")
    code = models.CharField(verbose_name="Agency Short Code", max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ResponseType(models.Model):

    name = models.CharField(max_length=50, verbose_name="Agency Name")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Organisation(models.Model):
    name = models.CharField(max_length=50, verbose_name="Organisation")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class InvestigationType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Investigation Type")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class LegalResultType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Legal Result Type")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PublicDamageType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Public Damage Type")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PrivateDamageType(models.Model):
    name = models.CharField(max_length=25, verbose_name="Private Damage Type")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

#@python_2_unicode_compatible
#class InitialActivityType(models.Model):
#    name = models.CharField(max_length=25, verbose_name="Activity Type")
#
#    class Meta:
#        ordering = ['name']
#
#    def __str__(self):
#        return self.name


@python_2_unicode_compatible
class ActivityType(models.Model):
    name = models.CharField(max_length=25, verbose_name="Activity Type")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name




"""
Point of Origin
"""
#@python_2_unicode_compatible
#class InitialLocation(models.Model):
#    distance = models.DecimalField(
#        verbose_name="Distance (km)", max_digits=6, decimal_places=1,
#        validators=[MinValueValidator(0)])
#    direction = models.OneToOneField(Direction, verbose_name="Direction")
#    place = models.CharField(max_length=25)
#    lot_no = models.CharField(verbose_name="Lot Number", max_length=10)
#    street = models.CharField(max_length=25)
#    town = models.CharField(max_length=25)
#    initial_bushfire = models.OneToOneField(InitialBushfire, related_name='initial_location')
#
#    def __str__(self):
#        return self.direction.name


#@python_2_unicode_compatible
#class InitialOrigin(models.Model):
#    COORD_TYPE_1 = 1
#    COORD_TYPE_2 = 2
#    COORD_TYPE_3 = 3
#    COORD_TYPE_CHOICES = (
#        (COORD_TYPE_1, 'MGA'),
#        (COORD_TYPE_2, 'Lat/Long'),
#        (COORD_TYPE_3, 'FD Grid'),
#    )
#
#    coord_type = models.PositiveSmallIntegerField(choices=COORD_TYPE_CHOICES, verbose_name="Coordinate Type")
#    fire_not_found = models.BooleanField(default=False)
#    # TODO number of dp
#    lat_decimal = models.DecimalField(verbose_name="Latitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lat_degrees = models.DecimalField(verbose_name="Latitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lat_minutes = models.DecimalField(verbose_name="Latitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lon_decimal = models.DecimalField(verbose_name="Longitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lon_degrees = models.DecimalField(verbose_name="Longitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    lon_minutes = models.DecimalField(verbose_name="Longitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#
#    mga_zone = models.DecimalField(verbose_name="MGA Zone", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    mga_easting = models.DecimalField(verbose_name="MGA Easting", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#    mga_northing = models.DecimalField(verbose_name="MGA Northing", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
#
#    fd_letter = models.CharField(verbose_name="FD Letter", max_length=2, null=True, blank=True)
#    fd_number = models.PositiveSmallIntegerField(verbose_name="FD Number", null=True, blank=True)
#    fd_tenths = models.CharField(verbose_name="FD Tenths", max_length=2, null=True, blank=True)
#
#    initial_bushfire = models.OneToOneField(InitialBushfire, related_name='initial_origin')
#
#
#    def __str__(self):
#        return self.get_coord_type_display()

@python_2_unicode_compatible
class Location(models.Model):
    distance = models.DecimalField(
        verbose_name="Distance (km)", max_digits=6, decimal_places=1,
        validators=[MinValueValidator(0)])
    direction = models.ForeignKey(Direction, verbose_name="Direction")
    place = models.CharField(max_length=25)
    lot_no = models.CharField(verbose_name="Lot Number", max_length=10)
    street = models.CharField(max_length=25)
    town = models.CharField(max_length=25)
    bushfire = models.OneToOneField(Bushfire, related_name='location')

    def __str__(self):
        return self.direction.name


@python_2_unicode_compatible
class Origin(models.Model):
    COORD_TYPE_1 = 1
    COORD_TYPE_2 = 2
    COORD_TYPE_3 = 3
    COORD_TYPE_CHOICES = (
        (COORD_TYPE_1, 'MGA'),
        (COORD_TYPE_2, 'Lat/Long'),
        (COORD_TYPE_3, 'FD Grid'),
    )

    coord_type = models.PositiveSmallIntegerField(choices=COORD_TYPE_CHOICES, verbose_name="Coordinate Type")
    fire_not_found = models.BooleanField(default=False)
    # TODO number of dp
    lat_decimal = models.DecimalField(verbose_name="Latitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lat_degrees = models.DecimalField(verbose_name="Latitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lat_minutes = models.DecimalField(verbose_name="Latitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_decimal = models.DecimalField(verbose_name="Longitude (Decimal)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_degrees = models.DecimalField(verbose_name="Longitude (Degrees)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    lon_minutes = models.DecimalField(verbose_name="Longitude (Minutes)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)

    mga_zone = models.DecimalField(verbose_name="MGA Zone", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    mga_easting = models.DecimalField(verbose_name="MGA Easting", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)
    mga_northing = models.DecimalField(verbose_name="MGA Northing", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)], null=True, blank=True)

    fd_letter = models.CharField(verbose_name="FD Letter", max_length=2, null=True, blank=True)
    fd_number = models.PositiveSmallIntegerField(verbose_name="FD Number", null=True, blank=True)
    fd_tenths = models.CharField(verbose_name="FD Tenths", max_length=2, null=True, blank=True)

    bushfire = models.OneToOneField(Bushfire, related_name='origin')


    def __str__(self):
        return self.get_coord_type_display()


"""
Effects/Agencies
"""
class Effect(models.Model):
    frb_effect = models.ForeignKey('FrbEffect', verbose_name='Presence/Effect of FRB', null=True, blank=True)
    fire_stopped = models.PositiveSmallIntegerField(verbose_name="Fuel Age - Fire Stopped (Yr)", null=True, blank=True)
    waterbomb_effect = models.ForeignKey('WaterBombEffect', verbose_name='Presence/Effect of WaterBomb', null=True, blank=True)
    last_burnt = models.PositiveSmallIntegerField(verbose_name="Fuel Age - Area Last Burnt (Yr)", null=True, blank=True)
    arrival_area = models.DecimalField(verbose_name="Fire Area at Arrival (ha)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)])
    fire_level = models.PositiveSmallIntegerField(verbose_name='Final Fire Level', choices=FIRE_LEVEL_CHOICES)
    rating = models.ForeignKey('PriorityRating', verbose_name="Area Priority Rating")
    bushfire = models.OneToOneField(Bushfire, related_name='effects')

    def __str__(self):
        return self.frb_effect.name


@python_2_unicode_compatible
class Response(models.Model):
    bushfire = models.ForeignKey(Bushfire, related_name='responses')
    response = models.ForeignKey(ResponseType)
    #response = models.PositiveSmallIntegerField(choices=RESPONSE_CHOICES)

    def __str__(self):
        return self.response

    class Meta:
        unique_together = ('bushfire', 'response',)


#@python_2_unicode_compatible
#class FirstAttackAgency(models.Model):
#    bushfire = models.ForeignKey(Bushfire, related_name='first_attack_agencies')
#    agency = models.PositiveSmallIntegerField(choices=Agency)
#
#    def __str__(self):
#        return self.agency


@python_2_unicode_compatible
class FirstAttackAgency(models.Model):

    first_attack = models.ForeignKey(Agency, verbose_name="First Attack Agency", related_name='first_attack')
    hazard_mgt = models.ForeignKey(Agency, verbose_name="Hazard Management Agency", null=True, blank=True, related_name='hazard_mgt')
    initial_control = models.ForeignKey(Agency, verbose_name="Initial Controlling Agency", null=True, blank=True, related_name='initial_control')
    final_control = models.ForeignKey(Agency, verbose_name="Final Controlling Agency", null=True, blank=True, related_name='final_control')
    bushfire = models.OneToOneField(Bushfire, related_name='first_attack')

    def __str__(self):
        l = []
        if self.first_attack:
            l.append('First Attack Agency: {}'.format(self.first_attack))
        if self.hazard_mgt:
            l.append('Hazard Management Agency: {}'.format(self.hazard_mgt))
        if self.initial_control:
            l.append('Initial Control Agency: {}'.format(self.initial_control))
        if self.final_control:
            l.append('Final Control Agency: {}'.format(self.final_control))
        return ', '.join(l)


"""
Area Burnt/Forces
"""
@python_2_unicode_compatible
class AreaBurnt(models.Model):
    tenure = models.ForeignKey(Tenure, related_name='tenures')
    fuel_type = models.ForeignKey(FuelType, related_name='fuel_types') # vegetation_type was renamed to fuel_type in PBS
    area = models.DecimalField(verbose_name="Area (ha)", max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    origin = models.BooleanField(verbose_name="Point of Origin", default=False)
    bushfire = models.ForeignKey(Bushfire, related_name='areas_burnt')

    def clean(self):
        if self.bushfire.areas_burnt.all().count() == 0:
            raise ValidationError("You must enter one Area Burnt record")

    def __str__(self):
        return 'Tenure: {}, Fuel Type: {}, Area: {}, Origin: {}'.format(
            self.tenure.name, self.fuel_type.name, self.area, self.origin)

    class Meta:
        unique_together = ('bushfire', 'tenure', 'fuel_type',)


@python_2_unicode_compatible
class GroundForces(models.Model):
    GF_AGENCY_CHOICES = (
        (1, 'Initial DEC Dispatch'),
        (2, 'DEC Peak'),
        (3, 'Other Agencies Peak'),
    )

    name = models.PositiveSmallIntegerField(choices=GF_AGENCY_CHOICES, verbose_name="Agency Name", null=True, blank=True)
    persons = models.PositiveSmallIntegerField(null=True, blank=True)
    pumpers = models.PositiveSmallIntegerField(null=True, blank=True)
    plant = models.PositiveSmallIntegerField(null=True, blank=True)
    bushfire = models.ForeignKey(Bushfire, related_name='ground_forces')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('bushfire', 'name',)


@python_2_unicode_compatible
class AerialForces(models.Model):
    AF_AGENCY_CHOICES = (
        (1, 'Fixed Wing'),
        (2, 'Helicopter'),
    )

    name = models.PositiveSmallIntegerField(choices=AF_AGENCY_CHOICES, verbose_name="Agency Name", null=True, blank=True)
    observer = models.PositiveSmallIntegerField(null=True, blank=True)
    transporter = models.PositiveSmallIntegerField(null=True, blank=True)
    ignition = models.PositiveSmallIntegerField(null=True, blank=True)
    water_bomber = models.PositiveSmallIntegerField(null=True, blank=True)
    bushfire = models.ForeignKey(Bushfire, related_name='aerial_forces')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('bushfire', 'name',)

"""
Attendance/Behaviour
"""
@python_2_unicode_compatible
class FireBehaviour(models.Model):
    name = models.CharField(verbose_name="Name/Description", max_length=50, null=True, blank=True)
    fuel_type = models.ForeignKey(FuelType, related_name='fuel_types_fire', null=True, blank=True) # vegetation_type was renamed to fuel_type in PBS
    fuel_weight = models.PositiveSmallIntegerField(null=True, blank=True)
    fdi = models.PositiveSmallIntegerField(null=True, blank=True)
    ros = models.PositiveSmallIntegerField(null=True, blank=True)
    bushfire = models.ForeignKey(Bushfire, related_name='fire_behaviour')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('bushfire', 'name',)


@python_2_unicode_compatible
class AttendingOrganisation(models.Model):
    name = models.ForeignKey('Organisation', null=True, blank=True)
    other = models.CharField(max_length=25, null=True, blank=True)
    bushfire = models.ForeignKey(Bushfire, related_name='attending_organisations')

    def clean_name(self):
        if self.name == 'Other' and not self.other:
            raise ValidationError("You must enter 'Other' attending organisation")

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('bushfire', 'name',)


"""
Damages/Legal
"""
@python_2_unicode_compatible
class Legal(models.Model):
    protection = models.PositiveSmallIntegerField(verbose_name="Community Protection (%)", validators=[MinValueValidator(0), MaxValueValidator(100)])
    cost = models.DecimalField(verbose_name="Est. Cost of Damages ($)", max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    restricted_period = models.BooleanField(default=False)
    prohibited_period = models.BooleanField(default=False)
    inv_undertaken = models.ForeignKey(InvestigationType, verbose_name="Investigation Undertaken")
    legal_result = models.ForeignKey(LegalResultType)
    bushfire = models.ForeignKey(Bushfire, related_name='legal')

    def __str__(self):
        return self.legal_result.name


@python_2_unicode_compatible
class PublicDamage(models.Model):
    damage_type = models.ForeignKey(PublicDamageType)
    fuel_type = models.ForeignKey(FuelType)
    area = models.DecimalField(verbose_name="Area (ha)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)])
    bushfire = models.ForeignKey(Bushfire, related_name='public_damages')

    def __str__(self):
        return self.damage_type

    class Meta:
        unique_together = ('bushfire', 'damage_type', 'fuel_type',)


@python_2_unicode_compatible
class PrivateDamage(models.Model):
    damage_type = models.ForeignKey(PrivateDamageType)
    number = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    bushfire = models.ForeignKey(Bushfire, related_name='private_damages')

    def __str__(self):
        return self.damage_type

    class Meta:
        unique_together = ('bushfire', 'damage_type',)


"""
Final Comments
"""
@python_2_unicode_compatible
class Comment(Audit):
    comment = models.TextField()
    bushfire = models.ForeignKey(Bushfire, related_name='final_comments')

    def __str__(self):
        return self.damage_type


"""
Details
"""
#@python_2_unicode_compatible
#class InitialDetail(models.Model):
#    CAUSE_CHOICES = (
#        (1, 'Known'),
#        (2, 'Possible'),
#    )
#
#    tenure = models.ForeignKey(Tenure)
#    fuel_type = models.ForeignKey(FuelType)
#    area = models.DecimalField(verbose_name="Area (ha)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)])
#
#    first_attack = models.ForeignKey(Agency)
#    other_agency = models.CharField(verbose_name='Other', max_length=25, null=True, blank=True)
#
#    # TODO form must include AttendingOrganisation list (choices is common, but info is different)
#    dec = models.BooleanField(verbose_name="DEC", default=False)
#    lga_bfb = models.BooleanField(verbose_name="LGA BFB", default=False)
#    fesa = models.BooleanField(verbose_name="FESA", default=False)
#    ses = models.BooleanField(verbose_name="SES", default=False)
#    police = models.BooleanField(verbose_name="POLICE", default=False)
#    other_force = models.CharField(verbose_name='Other', max_length=25, null=True, blank=True)
#
#    cause = models.ForeignKey(Cause)
#    known_possible = models.PositiveSmallIntegerField(choices=CAUSE_CHOICES, verbose_name="Known/Possible")
#    other_cause = models.CharField(verbose_name='Other', max_length=25, null=True, blank=True)
#    investigation_req = models.BooleanField(verbose_name="Invest'n Required", default=False)
#    initial_bushfire = models.OneToOneField(InitialBushfire, related_name='initial_detail')
#
#    def clean_first_attack(self):
#        if self.first_attack == 'Other' and not self.other:
#            raise ValidationError("You must enter 'Other' First Attack Agency")
#
#    def __str__(self):
#        return self.tenure.name

@python_2_unicode_compatible
class Detail(models.Model):
    CAUSE_CHOICES = (
        (1, 'Known'),
        (2, 'Possible'),
    )

    tenure = models.ForeignKey(Tenure)
    fuel_type = models.ForeignKey(FuelType)
    area = models.DecimalField(verbose_name="Area (ha)", max_digits=12, decimal_places=1, validators=[MinValueValidator(0)])

    first_attack = models.ForeignKey(Agency)
    other_agency = models.CharField(verbose_name='Other', max_length=25, null=True, blank=True)

    # TODO form must include AttendingOrganisation list (choices is common, but info is different)
    dec = models.BooleanField(verbose_name="DEC", default=False)
    lga_bfb = models.BooleanField(verbose_name="LGA BFB", default=False)
    fesa = models.BooleanField(verbose_name="FESA", default=False)
    ses = models.BooleanField(verbose_name="SES", default=False)
    police = models.BooleanField(verbose_name="POLICE", default=False)
    other_force = models.CharField(verbose_name='Other', max_length=25, null=True, blank=True)

    cause = models.ForeignKey(Cause)
    known_possible = models.PositiveSmallIntegerField(choices=CAUSE_CHOICES, verbose_name="Known/Possible")
    other_cause = models.CharField(verbose_name='Other', max_length=25, null=True, blank=True)
    investigation_req = models.BooleanField(verbose_name="Invest'n Required", default=False)
    bushfire = models.OneToOneField(Bushfire, related_name='detail')

    def clean(self):
        import ipdb; ipdb.set_trace()

        if self.first_attack.name == 'OTHER' and not self.other_agency:
            raise ValidationError("You must enter 'Other' Forces Agency")

        if not (self.dec and self.lga_bfb and self.fesa and self.police) and len(self.other_force)==0:
            raise ValidationError("You must specify an Attending Organisation or Other")

        if self.cause.name == 'OTHER' and not self.other_cause:
            raise ValidationError("You must enter 'Other' First Attack Agency")

    def __str__(self):
        return self.tenure.name


"""
Initial Comments
"""

@python_2_unicode_compatible
class Initial(Audit):
    fuel = models.CharField(max_length=50)
    ros = models.CharField(verbose_name="Rate of Spread", max_length=50)
    flame_height = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    assistance_required = models.CharField(max_length=50)
    fire_contained = models.BooleanField(default=False)
    containment_time = models.CharField(verbose_name="ET to Contain", max_length=50)
    ops_point = models.CharField(verbose_name="OPS Point (grid ref)", max_length=50)
    communications = models.CharField(verbose_name='Communication', max_length=50)
    weather = models.CharField(max_length=50)
    field_officer = models.ForeignKey(User, verbose_name="Field Officer", related_name='field_officer')
    authorised_by = models.ForeignKey(User, verbose_name="Authorising Officer", blank=True, null=True)
    authorised_date = models.DateTimeField(default=timezone.now)

    bushfire = models.OneToOneField(Bushfire, related_name='initial_report')

    def user_unicode_patch(self):
        """ overwrite the User model's __unicode__() method """
        if self.first_name or self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        return self.username
    User.__unicode__ = user_unicode_patch

    def __str__(self):
        return self.field_officer.get_full_name()


"""
Main Area
"""
#@python_2_unicode_compatible
#class InitialActivity(models.Model):
#    #activity = models.PositiveSmallIntegerField(choices=ACTIVITY_CHOICES)
#    activity = models.ForeignKey(InitialActivityType)
#    date = models.DateTimeField(default=timezone.now)
#    bushfire = models.ForeignKey(InitialBushfire, related_name='initial_activities')
#
#    class Meta:
#        ordering = ['activity']
#
#    def __str__(self):
#        return self.activity.name
#
#    class Meta:
#        unique_together = ('bushfire', 'activity',)


@python_2_unicode_compatible
class Activity(models.Model):
    #activity = models.PositiveSmallIntegerField(choices=ACTIVITY_CHOICES)
    activity = models.ForeignKey(ActivityType)
    date = models.DateTimeField(default=timezone.now)
    bushfire = models.ForeignKey(Bushfire, related_name='activities')

    class Meta:
        ordering = ['activity']

    def __str__(self):
        return self.activity.name

    class Meta:
        unique_together = ('bushfire', 'activity',)


@python_2_unicode_compatible
class Reporter(models.Model):

    source = models.ForeignKey(Source, verbose_name="Reported By", null=True, blank=True)
    cause = models.ForeignKey(Cause)
    arson_squad_notified = models.BooleanField(verbose_name="Arson Squad Notified", default=False)
    #prescription = models.ForeignKey(Prescription, verbose_name="ePFP (if cause is Escape)", related_name='prescribed_burn', null=True, blank=True)
    prescription = models.ForeignKey(Prescription, verbose_name="Prescription Burn ID", null=True, blank=True)
    offence_no = models.CharField(verbose_name="Offence No.", max_length=10)
    bushfire = models.OneToOneField(Bushfire, related_name='reporting')

    def __str__(self):
        return self.offence_no


#@python_2_unicode_compatible
#class InitialAuthorisation(Audit):
#    name = models.ForeignKey(User)
#    date = models.DateTimeField(default=timezone.now)
#    initial_bushfire = models.OneToOneField(InitialBushfire, related_name='initial_authorisation')
#
#    def __str__(self):
#        #import ipdb; ipdb.set_trace()
#        return '{} {}'.format(self.name.get_full_name(), self.date)


#@python_2_unicode_compatible
#class Authorisation(Audit):
#    name = models.ForeignKey(User)
#    date = models.DateTimeField(default=timezone.now)
#    bushfire = models.OneToOneField(Bushfire, related_name='authorisation')
#
#    def __str__(self):
#        #import ipdb; ipdb.set_trace()
#        return '{} {}'.format(self.name.get_full_name(), self.date)




