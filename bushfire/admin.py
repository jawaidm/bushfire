from django.contrib import admin
from bushfire.models import Bushfire, Comment, FinalComment, PrivateDamage, Activity, Authorisation
from tabbed_admin import TabbedModelAdmin


#class CommentInline(admin.TabularInline):
#    model = Comment
#
#class BushfireAdmin(admin.ModelAdmin):
#    inlines = [
#        CommentInline
#    ]




class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class FinalCommentInline(admin.TabularInline):
    model = FinalComment
    extra = 0


class PrivateDamageInline(admin.TabularInline):
    model = PrivateDamage
    extra = 0

class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0


class AuthorisationInline(admin.TabularInline):
    model = Authorisation
    extra = 0

    fields = ('name', 'auth_type', 'date')



class BushfireAdmin(TabbedModelAdmin):
    model = Bushfire

    tab_overview = (
        (None, {'fields': ('district', 'incident_no', 'season', 'job_code', 'name', 'potential_fire_level')}),
        ActivityInline,
        AuthorisationInline,
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

admin.site.register(Bushfire, BushfireAdmin)
#admin.site.register(PrivateDamage, PrivateDamageAdmin)

