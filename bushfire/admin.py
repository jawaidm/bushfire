from django.contrib import admin
from bushfire.models import (Bushfire, Comment, FinalComment, PrivateDamage, PublicDamage,
        Activity, Authorisation, Origin, Detail, Location, Effect, Response,
        FirstAttackAgency, AreaBurnt, GroundForces, AerialForces, FireBehaviour,
        AttendingOrganisation, Legal, Reporter)
from tabbed_admin import TabbedModelAdmin
from merged_inlines.admin import MergedInlineAdmin


#class CommentInline(admin.TabularInline):
#    model = Comment
#


class OriginInline(admin.StackedInline):
    model = Origin
    suit_classes = 'suit-tab suit-tab-origin'
#    fields = (('lat_decimal', 'lat_degrees', 'lat_minutes'), ('lon_decimal', 'lon_degrees', 'lon_minutes'),)
    fieldsets = [
        (None, {'fields': [('coord_type', 'fire_not_found')]}),
        ('Lat/Long', {'fields': [('lat_decimal', 'lat_degrees', 'lat_minutes'), ('lon_decimal', 'lon_degrees', 'lon_minutes')]}),
        ('MGA', {'fields': [('mga_zone', 'mga_easting', 'mga_northing')]}),
        ('FD Grid', {'fields': [('fd_letter', 'fd_number', 'fd_tenths')], 'classes': ['collapse',]}),
    ]
    #max_num = 0
    #extra = 0
    verbose_name = "Origin"
    verbose_name_plural = "Origins"


class DetailInline(admin.StackedInline):
    model = Detail
    suit_classes = 'suit-tab suit-tab-detail'
    fieldsets = [
        ('Tenure and Vegetation Affected', {'fields': [('tenure', 'fuel_type', 'area')]}),
        ('Forces', {'fields': [('first_attack', 'other_agency'), ('dec', 'lga_bfb', 'fesa', 'ses', 'police', 'other_force')]}),
        ('Miscellaneous', {'fields': [('cause', 'known_possible', 'other_cause', 'investigation_req')]}),
    ]

    def has_delete_permission(self, request, obj=None):
        return False

class CommentInline(admin.StackedInline):
    model = Comment
    suit_classes = 'suit-tab suit-tab-ini_comment'
    fieldsets = [
        ('Miscellaneous', {'fields': [('fuel'), ('ros'), ('flame_height'), ('assistance_required'),
        ('containment_time', 'fire_contained'), ('ops_point'), ('communications'), ('weather'), ('field_officer')]}),
    ]
    #extra = 0



class PrivateDamageInline(admin.TabularInline):
    model = PrivateDamage
    suit_classes = 'suit-tab suit-tab-pri_damage'
    extra = 0


class PublicDamageInline(admin.TabularInline):
    model = PublicDamage
    suit_classes = 'suit-tab suit-tab-pub_damage'
    extra = 0


class ActivityInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-activities'
    model = Activity
    extra = 0
    verbose_name_plural = "Activities"


class AuthorisationInline(admin.TabularInline):
    model = Authorisation
    suit_classes = 'suit-tab suit-tab-auth'
    extra = 0

    fields = ('name', 'auth_type', 'date')

class LocationInline(admin.StackedInline):
    suit_classes = 'suit-tab suit-tab-location'
    model = Location
    fields = (('distance', 'direction', 'place'), ('lot_no', 'street', 'town'),)
    #extra = 0


class EffectInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-effect'
    model = Effect
    extra = 0


class ResponseInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-response'
    model = Response
    extra = 0


class FirstAttackAgencyInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-first_attack_agency'
    model = FirstAttackAgency
    extra = 0


class AreaBurntInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-area_burnt'
    model = AreaBurnt
    extra = 0


class GroundForcesInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-ground_forces'
    model = GroundForces
    extra = 0


class AerialForcesInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-aerial_forces'
    model = AerialForces
    extra = 0


class FireBehaviourInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-fire_behaviour'
    model = FireBehaviour
    extra = 0


class AttendingOrganisationInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-attending_org'
    model = AttendingOrganisation
    extra = 0


class LegalInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-legal'
    model = Legal
    extra = 0


class ReporterInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-reporter'
    model = Reporter
    extra = 0


class FinalCommentInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-fin_comment'
    model = FinalComment
    extra = 0


class MyModelAdmin(MergedInlineAdmin):
    inlines = [OriginInline,LocationInline]


class _BushfireAdmin(admin.ModelAdmin):
    model = Bushfire
    list_display = ['district', 'incident_no', 'season', 'job_code', 'name', 'potential_fire_level', 'get_tenure'] #, 'authorised_by', 'get_auth_date']
    _fields = ('district', 'incident_no', 'season', 'job_code', 'name', 'potential_fire_level')

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': _fields
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('district', 'get_district')
        }),

        (None, {
            'classes': ('suit-tab', 'suit-tab-origin',),
            'fields': ('district', 'season')
            #'fields': _fields
        }),
#        (None, {
            #'classes': ('suit-tab', 'suit-tab-detail',),
            #'fields': _fields
#        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-comment',),
            'fields': _fields
        }),


    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('origin', 'Point of Origin'),
        #('detail', 'Detail'),
        #('comment', 'Comment'),
        #('auth', 'Auth'),
        #('info', 'Info on tabs')
    )

#    inlines = [
        #OriginInline,
        #DetailInline,
        #CommentInline,
        #AuthorisationInline,
#    ]

    def get_auth_date(self, obj):
        return obj.authorised_by.date
    get_auth_date.admin_order_field  = 'authorised_by'  #Allows column order sorting
    get_auth_date.short_description = 'Date'

    def get_direction(self):
        return self.location.place
    get_direction.admin_order_field  = 'location'  #Allows column order sorting
    get_direction.short_description = 'Direction'

    def get_tenure(self, obj):
        return obj.detail.tenure.name
    get_tenure.admin_order_field  = 'detail'  #Allows column order sorting
    get_tenure.short_description = 'Tenure'

    def get_district(self, obj):
        return obj.district.name
    get_district.admin_order_field  = 'district'  #Allows column order sorting
    get_district.short_description = 'District'


class BushfireAdmin(TabbedModelAdmin):
    model = Bushfire
    list_display = ['district', 'incident_no', 'season', 'job_code', 'name', 'potential_fire_level' ]

    tab_overview = (
        (None, {'fields': (('region', 'district'), ('incident_no', 'season', 'job_code'), ('name', 'potential_fire_level'))}),
        ActivityInline,
        AuthorisationInline,
    )

    tab_origin = (
        OriginInline,
        LocationInline,
    )

    tab_detail = (
        DetailInline,
    )

    tab_comment = (
        CommentInline,
    )

    tab_damage = (
        PrivateDamageInline,
        FinalCommentInline
    )

    tabs = [
        ('Overview', tab_overview),
        ('Point of Origin', tab_origin),
        ('Detail', tab_detail),
        ('Comment', tab_comment),
    ]

    def get_auth_date(self, obj):
        return obj.authorised_by.date
    get_auth_date.admin_order_field  = 'authorised_by'  #Allows column order sorting
    get_auth_date.short_description = 'Date'

admin.site.register(Bushfire, BushfireAdmin)
#admin.site.register(PrivateDamage, PrivateDamageAdmin)
