from django import forms
from bushfire.models import (Bushfire, Activity, Response, AreaBurnt, GroundForces, AerialForces,
        AttendingOrganisation, FireBehaviour, Legal, PrivateDamage, PublicDamage, Comment,
        Region, District
    )
from datetime import datetime, timedelta
from django.conf import settings
from django.forms import ValidationError
from django.forms.models import inlineformset_factory, formset_factory, BaseInlineFormSet
#from django.forms.formsets import BaseFormSet
from django.contrib import messages

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from crispy_forms.bootstrap import TabHolder, Tab


class _ActivityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        super(_ActivityForm, self).__init__(*args, **kwargs)

#        self.helper = FormHelper()
##        self.helper.form_method = 'post'
#
#        self.helper.layout = Layout(
#            Div(
#                Div('activity',css_class='col-sm-2',),
#                Div('date',css_class='col-sm-2',),
#                css_class='row',
#            ),
#        )

#    def clean(self):
#        """
#        Adds validation to check that no two links have the same anchor or URL
#        and that all links have both an anchor and URL.
#        """
#        import ipdb; ipdb.set_trace()
#        if any(self.errors):
#            return
#
#        activities = []
#        dates = []
#        duplicates = False
#
#        for form in self.forms:
#            if form.cleaned_data:
#                activity = form.cleaned_data['activity']
#                date = form.cleaned_data['date']
#
#                # Check that no two links have the same anchor or URL
#                if activity:
#                    if activity in activities:
#                        duplicates = True
#                    activities.append(activity)
#
#                if duplicates:
#                    raise forms.ValidationError(
#                        'Activities must have unique.',
#                        code='duplicate_activity'
#                    )
#
#                # Check that all links have both an anchor and URL
#                if activity and not date:
#                    raise forms.ValidationError(
#                        'All Activities must have a date',
#                        code='missing_date'
#                    )
#                elif date and not activity:
#                    raise forms.ValidationError(
#                        'All Activities must have both an activity and date.',
#                        code='missing_date'
#                    )



    class Meta:
        model = Activity
        fields = ('activity', 'date',)


class _BushfireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        if kwargs.has_key('user'):
            user = kwargs.pop('user')
        super(BushfireForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
#        self.helper.form_class = 'form-horizontal'
#        self.helper.label_class = 'col-sm-2'
#        self.helper.field_class = 'col-sm-8'

        self.helper.layout = Layout(
            Div(
                Div('region',css_class='col-sm-2',),
                Div('district',css_class='col-sm-2',),
                Div('incident_no',css_class='col-sm-2',),
                Div('season',css_class='col-sm-2',),
                Div('job_code',css_class='col-sm-2',),
                css_class='row',
            ),
            Div(
                Div('name',css_class='col-sm-2',),
                Div('dfes_incident_no',css_class='col-sm-2',),
                Div('potential_fire_level',css_class='col-sm-2',),
                Div('authorised_by',css_class='col-sm-2',),
                Div('authorised_date',css_class='col-sm-2',),
                css_class='row',
            ),


            TabHolder(
                self.add_origin(),
                self.add_location(),
                #self.add_activities(),
                Tab(
                    'PlaceHolder',
                    #'location2',
                ),
#                Tab(
#                    'Location',
#                    Div(
#                        Div('distance',css_class='col-sm-2',),
#                        Div('direction',css_class='col-sm-2',),
#                        Div('place',css_class='col-sm-4',),
#                        Div('lot_no',css_class='col-sm-2',),
#                        css_class='row',
#                    ),
#                    Div(
#                        Div('street',css_class='col-sm-4',),
#                        Div('town',css_class='col-sm-2',),
#                        css_class='row',
#                    ),
#                ),
            ),

#            ButtonHolder(
#                Submit('submit', 'Submit', css_class='button white')
#            )

        )

    def add_origin(self):
        return Tab(
            'Point of Origin',
            Div(
                Div('coord_type',css_class='col-sm-2',),
                Div('fire_not_found',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),
            Div(
                Div(
                    Div('lat_decimal',css_class='col-sm-2',),
                    Div('lat_degrees',css_class='col-sm-2',),
                    Div('lat_minutes',css_class='col-sm-2',),
                    css_class='row',
                ),
                Div(
                    Div('lon_decimal',css_class='col-sm-2',),
                    Div('lon_degrees',css_class='col-sm-2',),
                    Div('lon_minutes',css_class='col-sm-2',),
                    css_class='row',
                ),
            ),
            HTML('<hr>'),
            Div(
                Div('mga_zone',css_class='col-sm-2',),
                Div('mga_easting',css_class='col-sm-2',),
                Div('mga_northing',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),
            Div(
                Div('fd_letter',css_class='col-sm-2',),
                Div('fd_number',css_class='col-sm-2',),
                Div('fd_tenths',css_class='col-sm-2',),
                css_class='row',
            ),
            HTML('<hr>'),

        )

    def add_location(self):
        return Tab(
            'Location',
            Div(
                Div('distance',css_class='col-sm-2',),
                Div('direction',css_class='col-sm-2',),
                Div('place',css_class='col-sm-4',),
                Div('lot_no',css_class='col-sm-2',),
                css_class='row',
            ),
            Div(
                Div('street',css_class='col-sm-4',),
                Div('town',css_class='col-sm-2',),
                css_class='row',
            ),
        )

    def add_activities(self):
        return Tab(
            'Activities',
            Div(
                Div('activity',css_class='col-sm-2',),
                Div('date',css_class='col-sm-2',),
            ),
        )
    class Meta:
        model = Bushfire
        #fields = ('region', 'district', 'incident_no', 'season', 'job_code',)
        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'dfes_incident_no', 'potential_fire_level', 'authorised_by', 'authorised_date',
                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
                  'coord_type', 'fire_not_found', 'lat_decimal', 'lat_degrees', 'lat_minutes',
                  'lon_decimal', 'lon_degrees', 'lon_minutes', 'mga_zone', 'mga_easting', 'mga_northing',
                  'fd_letter', 'fd_number', 'fd_tenths',
                 )


class BushfireForm(forms.ModelForm):
    class Meta:
        model = Bushfire
#        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
#                  'name', 'dfes_incident_no', 'potential_fire_level', 'authorised_by', 'authorised_date',
#                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
#                  'coord_type', 'fire_not_found', 'lat_decimal', 'lat_degrees', 'lat_minutes',
#                  'lon_decimal', 'lon_degrees', 'lon_minutes', 'mga_zone', 'mga_easting', 'mga_northing',
#                  'fd_letter', 'fd_number', 'fd_tenths',
#                  'source','cause', 'arson_squad_notified', 'prescription', 'offence_no',
#                  'fuel','ros', 'flame_height', 'assistance_required', 'fire_contained', 'containment_time',
#                  'ops_point', 'communications', 'weather', 'field_officer', 'init_authorised_by', 'init_authorised_date',
#                 )
        exclude = ()


class BushfireCreateForm(forms.ModelForm):
    class Meta:
        model = Bushfire
        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'potential_fire_level', 'init_authorised_by', 'init_authorised_date',
                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
                  'coord_type', 'fire_not_found',
                  'lat_decimal', 'lat_degrees', 'lat_minutes', 'lon_decimal', 'lon_degrees', 'lon_minutes',
                  'mga_zone', 'mga_easting', 'mga_northing',
                  'fd_letter', 'fd_number', 'fd_tenths',
#                  'source','cause', 'arson_squad_notified', 'prescription', 'offence_no',
                  'fuel','ros', 'flame_height', 'assistance_required', 'fire_contained',
                  'containment_time', 'ops_point', 'communications', 'weather', 'field_officer',
                  'first_attack', 'other_agency',
                  'cause', 'known_possible', 'other_cause', 'investigation_req',
                 )

    def clean(self):
        import ipdb; ipdb.set_trace()
        district = self.cleaned_data['district']
        incident_no = self.cleaned_data['incident_no']
        season = self.cleaned_data['season']
        bushfire = Bushfire.objects.filter(district=district, season=season, incident_no=incident_no)
        if bushfire:
            raise ValidationError('There is already a Bushfire with this District, Season and Incident No. {} - {} - {}'.format(district, season, incident_no))
        else:
            return self.cleaned_data

class BushfireInitUpdateForm(forms.ModelForm):
    class Meta:
        model = Bushfire
        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'potential_fire_level', 'init_authorised_by', 'init_authorised_date',
                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
                  'coord_type', 'fire_not_found',
                  'lat_decimal', 'lat_degrees', 'lat_minutes', 'lon_decimal', 'lon_degrees', 'lon_minutes',
                  'mga_zone', 'mga_easting', 'mga_northing',
                  'fd_letter', 'fd_number', 'fd_tenths',
#                  'source','cause', 'arson_squad_notified', 'prescription', 'offence_no',
                  'fuel','ros', 'flame_height', 'assistance_required', 'fire_contained',
                  'containment_time', 'ops_point', 'communications', 'weather', 'field_officer',
                  'first_attack', 'other_agency',
                  'cause', 'known_possible', 'other_cause', 'investigation_req',
                 )

    def clean(self):
        """
        Form can be saved prior to sign-off, without checking req'd fields.
        Required fields are checked during Authorisation sign-off, therefore checking and adding error fields manually
        """
        req_fields = [
            #'region', 'district', 'incident_no', 'season', # these are delcared Required in models.py
            'name', 'potential_fire_level', 'init_authorised_by', 'init_authorised_date',
            'first_attack',
            'cause',
            'field_officer',
            'known_possible',
        ]

        req_dep_fields = { # required dependent fields
            'first_attack': 'other_agency',
            'cause': 'other_cause',
            'coord_type': {
                'MGA': ['MGA Zone','MGA Easting','MGA Northing'],
                }
        }

        req_coord_fields = {
            'MGA': ['mga_zone','mga_easting','mga_northing'],
            'FD Grid': ['fd_letter','fd_number','fd_tenths'],
            'Lat/Long': ['lat_decimal','lat_degrees','lat_minutes', 'lon_decimal','lon_degrees','lon_minutes'],
        }

        req_activity_fields = [
            'FIRE DETECTED',
            'FIRE REPORT COMPILED',
        ]

        if self.cleaned_data['init_authorised_by']:
            # check all required fields
            #import ipdb; ipdb.set_trace()
            [self.add_error(field, 'This field is required.') for field in req_fields if not self.cleaned_data.has_key(field) or not self.cleaned_data[field]]

            # check if 'Other' has been selected from drop down and field has been set
            for field in req_dep_fields.keys():
                if self.cleaned_data.has_key(field) and 'other' in str(self.cleaned_data[field]).lower():
                    other_field = self.cleaned_data[req_dep_fields[field]]
                    if not other_field:
                        self.add_error(req_dep_fields[field], 'This field is required.')

            coord_type = [i[1] for i in Bushfire.COORD_TYPE_CHOICES if i[0]==self.cleaned_data['coord_type']]
            if coord_type:
                #import ipdb; ipdb.set_trace()
                for field in req_coord_fields[coord_type[0]]:
                    if self.cleaned_data.has_key(field) and not self.cleaned_data[field]:
                        self.add_error(field, 'This field is required.')

            #import ipdb; ipdb.set_trace()
            #if missing_fields:
            #    raise ValidationError('Cannot Authorise, must input required fields: {}'.format(', '.join([i.replace('_', ' ').title() for i in missing_fields])))


from bushfire.models import (BushfireTest2, Activity2)
class BushfireCreateForm2(forms.ModelForm):
    class Meta:
        model = BushfireTest2
        fields = ('region', 'district', 'incident_no', 'season', 'job_code',
                  'name', 'potential_fire_level', 'init_authorised_by', 'init_authorised_date',
#                  'distance', 'direction', 'place', 'lot_no', 'street', 'town',
#                  'coord_type', 'fire_not_found',
#                  'lat_decimal', 'lat_degrees', 'lat_minutes', 'lon_decimal', 'lon_degrees', 'lon_minutes',
#                  'mga_zone', 'mga_easting', 'mga_northing',
#                  'fd_letter', 'fd_number', 'fd_tenths',
##                  'source','cause', 'arson_squad_notified', 'prescription', 'offence_no',
#                  'fuel','ros', 'flame_height', 'assistance_required', 'fire_contained',
#                  'containment_time', 'ops_point', 'communications', 'weather', 'field_officer',
#                  'first_attack', 'other_agency',
#                  'cause', 'known_possible', 'other_cause', 'investigation_req',
                 )


from bushfire.models import (BushfireTest)
class BushfireTestForm(forms.ModelForm):
    class Meta:
        model = BushfireTest
        fields = ('region', 'district')


class BaseActivityFormSet(BaseInlineFormSet):
    def clean(self):
        """
        Adds validation to check:
            1. no duplicate activities
            2. required activities have been selected
        """
        #import ipdb; ipdb.set_trace()
        if any(self.errors):
            import ipdb; ipdb.set_trace()
            return

        activities = []
        dates = []
        duplicates = False
        required_activities = ['FIRE DETECTED*', 'FIRE REPORT COMPILED*']

        #import ipdb; ipdb.set_trace()
        for form in self.forms:
            if form.cleaned_data:
                activity = form.cleaned_data['activity'] if form.cleaned_data.has_key('activity') else None
                date = form.cleaned_data['date'] if form.cleaned_data.has_key('date') else None
                remove = form.cleaned_data['DELETE'] if form.cleaned_data.has_key('DELETE') else False

                if not remove:
                    # Check that no two records have the same activity
                    if activity:
                        if activity.name in activities:
                            duplicates = True
                        activities.append(activity.name)

                    if duplicates:
                        form.add_error('activity', 'Duplicate: must be unique')

        # check required activities have been selected, only when main form has been authorised
        if self.data['init_authorised_by']:
            if not set(required_activities).issubset(activities) and self.forms:
                form.add_error('__all__', 'Must select required Activities: {}'.format(', '.join(required_activities)))


class BaseAreaBurntFormSet(BaseInlineFormSet):
    def clean(self):
        """
        Adds validation to check:
            1. no duplicate (tenure, fuel_type) combination
        """
        if any(self.errors):
            return

        duplicates = False
        tenures = []

        #import ipdb; ipdb.set_trace()
        for form in self.forms:
            if form.cleaned_data:
                tenure = form.cleaned_data['tenure'] if form.cleaned_data.has_key('tenure') else None
                fuel_type = form.cleaned_data['fuel_type'] if form.cleaned_data.has_key('fuel_type') else None
                area = form.cleaned_data['area'] if form.cleaned_data.has_key('area') else None
                remove = form.cleaned_data['DELETE'] if form.cleaned_data.has_key('DELETE') else False

                if not remove:
                    # Check that no two records have the same (tenure and fuel_type) combination
                    if tenure and fuel_type and area:
                        if set([(tenure.name, fuel_type.name)]).issubset(tenures):
                            duplicates = True
                        tenures.append((tenure.name, fuel_type.name))

                    if duplicates:
                        form.add_error('tenure', 'Duplicate (Tenure - Fuel Type): must be unique')


class BaseAttendingOrganisationFormSet(BaseInlineFormSet):
    def clean(self):
        """
        Adds validation to check:
            1. no duplicate organisation
        """
        if any(self.errors):
            return

        duplicates = False
        organisations = []

        #import ipdb; ipdb.set_trace()
        for form in self.forms:
            if form.cleaned_data:
                name = form.cleaned_data['name'] if form.cleaned_data.has_key('name') else None
                other = form.cleaned_data['other'] if form.cleaned_data.has_key('other') else None
                remove = form.cleaned_data['DELETE'] if form.cleaned_data.has_key('DELETE') else False

                if not remove:
                    # Check that no two records have the same organisation (name)
                    if name:
                        if name in organisations:
                            duplicates = True
                        organisations.append(name)

                    if duplicates:
                        form.add_error('name', 'Duplicate Organisation: must be unique')

                    if 'other' in name.name.lower() and not other:
                        form.add_error('name', 'Must specify other organisation')





ActivityFormSet2            = inlineformset_factory(BushfireTest2, Activity2, extra=1, max_num=7, can_delete=True)
ActivityFormSet             = inlineformset_factory(Bushfire, Activity, formset=BaseActivityFormSet, extra=1, max_num=7,  min_num=2, can_delete=True)
ResponseFormSet             = inlineformset_factory(Bushfire, Response, extra=1, max_num=13, can_delete=True)
AreaBurntFormSet            = inlineformset_factory(Bushfire, AreaBurnt, formset=BaseAreaBurntFormSet, extra=1, can_delete=True)
GroundForcesFormSet         = inlineformset_factory(Bushfire, GroundForces, extra=1, max_num=3, can_delete=True)
AerialForcesFormSet         = inlineformset_factory(Bushfire, AerialForces, extra=1, max_num=2, can_delete=True)
#AttendingOrganisationFormSet= inlineformset_factory(Bushfire, AttendingOrganisation, extra=1, max_num=11, can_delete=True)
AttendingOrganisationFormSet= inlineformset_factory(Bushfire, AttendingOrganisation, formset=BaseAttendingOrganisationFormSet, extra=1, max_num=11, can_delete=True)
FireBehaviourFormSet        = inlineformset_factory(Bushfire, FireBehaviour, extra=1, can_delete=True)
LegalFormSet                = inlineformset_factory(Bushfire, Legal, extra=1, max_num=5*12, can_delete=True)
PrivateDamageFormSet        = inlineformset_factory(Bushfire, PrivateDamage, extra=1, max_num=12, can_delete=True)
PublicDamageFormSet         = inlineformset_factory(Bushfire, PublicDamage, extra=1, can_delete=True)
CommentFormSet              = inlineformset_factory(Bushfire, Comment, extra=1, can_delete=True)



