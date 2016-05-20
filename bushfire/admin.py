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


class OriginInline(admin.TabularInline):
    model = Origin
    suit_classes = 'suit-tab suit-tab-origin'
    extra = 0


class DetailInline(admin.StackedInline):
    model = Detail
    suit_classes = 'suit-tab suit-tab-detail'
    #fields = ('tenure', 'fuel_type', 'area')

#    fieldsets = [
        #(None,               {'fields': ['tenure', 'fuel_type']}),
        #('Date information', {'fields': ['area']}),
#    ]
    def has_delete_permission(self, request, obj=None):
        return False

class CommentInline(admin.TabularInline):
    model = Comment
    suit_classes = 'suit-tab suit-tab-ini_comment'
    extra = 0



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


class AuthorisationInline(admin.TabularInline):
    model = Authorisation
    suit_classes = 'suit-tab suit-tab-auth'
    extra = 0

    fields = ('name', 'auth_type', 'date')

class LocationInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-location'
    model = Location
    extra = 0


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


class BushfireAdmin(admin.ModelAdmin):
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
            'fields': ('district', 'season')
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
        #('general', 'General'),
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


class _BushfireAdmin(TabbedModelAdmin):
    model = Bushfire
    list_display = ['district', 'incident_no', 'season', 'job_code', 'name', 'potential_fire_level' ]

    tab_overview = (
        (None, {'fields': ('district', 'incident_no', 'season', 'job_code', 'name', 'potential_fire_level')}),
        ActivityInline,
    )
    tab_album = (
        (None, {
            'fields': ('district', 'name', 'incident_no', 'season')
        }),

        FinalCommentInline,
    )

    tab_extra = (
        (None, {
            'fields': ('district', 'name', 'incident_no', 'season')
        }),

        PrivateDamageInline,
    )

    tab_resources = (
        PrivateDamageInline,
        FinalCommentInline
    )

    tabs = [
        ('Overview', tab_overview),
        ('Albums', tab_album),
        ('Extra', tab_resources)
    ]

    def get_auth_date(self, obj):
        return obj.authorised_by.date
    get_auth_date.admin_order_field  = 'authorised_by'  #Allows column order sorting
    get_auth_date.short_description = 'Date'

admin.site.register(Bushfire, BushfireAdmin)
#admin.site.register(PrivateDamage, PrivateDamageAdmin)

