from bushfire.models import (Bushfire, Activity, AreaBurnt, AttendingOrganisation, GroundForces,
        AerialForces, FireBehaviour, Legal, PrivateDamage, PublicDamage, Response, Comment
    )
from django.db import IntegrityError, transaction

def breadcrumbs_li(links):
    """Returns HTML: an unordered list of URLs (no surrounding <ul> tags).
    ``links`` should be a iterable of tuples (URL, text).
    """
    crumbs = ''
    li_str = '<li><a href="{}">{}</a></li>'
    li_str_last = '<li class="active"><span>{}</span></li>'
    # Iterate over the list, except for the last item.
    if len(links) > 1:
        for i in links[:-1]:
            crumbs += li_str.format(i[0], i[1])
    # Add the last item.
    crumbs += li_str_last.format(links[-1][1])
    return crumbs


def calc_coords(obj):
        coord_type = obj.coord_type
        if coord_type == Bushfire.COORD_TYPE_MGAZONE:
            obj.lat_decimal = float(obj.mga_zone)/2.0
            obj.lat_degrees = float(obj.mga_zone)/2.0
            obj.lat_minutes = float(obj.mga_zone)/2.0

            obj.lon_decimal = float(obj.mga_zone)/2.0
            obj.lon_degrees = float(obj.mga_zone)/2.0
            obj.lon_minutes = float(obj.mga_zone)/2.0

        elif coord_type == Bushfire.COORD_TYPE_LATLONG:
            obj.mga_zone = float(obj.lat_decimal) * 2.0
            obj.mga_easting = float(obj.lat_decimal) * 2.0
            obj.mga_northing = float(obj.lat_decimal) * 2.0

# init methods
def update_activity_fs(bushfire, activity_formset):
    new_fs_object = []
    for form in activity_formset:
        if form.is_valid():
            activity = form.cleaned_data.get('activity')
            dt = form.cleaned_data.get('date')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (activity and dt):
                new_fs_object.append(Activity(bushfire=bushfire, activity=activity, date=dt))

    try:
        with transaction.atomic():
            #Replace the old with the new
            Activity.objects.filter(bushfire=bushfire).delete()
            Activity.objects.bulk_create(new_fs_object)
    except IntegrityError: #If the transaction failed
        return 0

    return 1


def update_areas_burnt_fs(bushfire, area_burnt_formset):
    new_fs_object = []
    for form in area_burnt_formset:
        if form.is_valid():
            tenure = form.cleaned_data.get('tenure')
            fuel_type = form.cleaned_data.get('fuel_type')
            area = form.cleaned_data.get('area')
            origin = form.cleaned_data.get('origin')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (tenure and fuel_type and area):
                new_fs_object.append(AreaBurnt(bushfire=bushfire, tenure=tenure, fuel_type=fuel_type, area=area, origin=origin))

    try:
        with transaction.atomic():
            AreaBurnt.objects.filter(bushfire=bushfire).delete()
            AreaBurnt.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_attending_org_fs(bushfire, attending_org_formset):
    new_fs_object = []
    for form in attending_org_formset:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            other = form.cleaned_data.get('other')
            remove = form.cleaned_data.get('DELETE')

            #if not remove and (name and other):
            if not remove and name:
                new_fs_object.append(AttendingOrganisation(bushfire=bushfire, name=name, other=other))

    try:
        with transaction.atomic():
            AttendingOrganisation.objects.filter(bushfire=bushfire).delete()
            AttendingOrganisation.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

# final methods
def update_groundforces_fs(bushfire, groundforces_formset):
    new_fs_object = []
    #groundforces_formset.cleaned_data # hack - form.cleaned_data is unavailable unless this is called
    for form in groundforces_formset:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            persons = form.cleaned_data.get('persons')
            pumpers = form.cleaned_data.get('pumpers')
            plant = form.cleaned_data.get('plant')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (name and persons and pumpers and plant):
                new_fs_object.append(GroundForces(bushfire=bushfire, name=name, persons=persons, pumpers=persons, plant=plant))

    try:
        with transaction.atomic():
            GroundForces.objects.filter(bushfire=bushfire).delete()
            GroundForces.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_aerialforces_fs(bushfire, aerialforces_formset):
    new_fs_object = []
    #aerialforces_formset.cleaned_data # hack - form.cleaned_data is unavailable unless this is called
    for form in aerialforces_formset:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            observer = form.cleaned_data.get('observer')
            transporter = form.cleaned_data.get('transporter')
            ignition = form.cleaned_data.get('ignition')
            water_bomber = form.cleaned_data.get('water_bomber')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (name and observer and transporter and ignition and water_bomber):
                new_fs_object.append(AerialForces(bushfire=bushfire, name=name, observer=observer, transporter=transporter, ignition=ignition, water_bomber=water_bomber))

    try:
        with transaction.atomic():
            AerialForces.objects.filter(bushfire=bushfire).delete()
            AerialForces.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_fire_behaviour_fs(bushfire, fire_behaviour_formset):
    new_fs_object = []
    for form in fire_behaviour_formset:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            fuel_type = form.cleaned_data.get('fuel_type')
            fuel_weight = form.cleaned_data.get('fuel_weight')
            fdi = form.cleaned_data.get('fdi')
            ros = form.cleaned_data.get('ros')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (name and fuel_type and fuel_weight and fdi and ros):
                new_fs_object.append(FireBehaviour(bushfire=bushfire, name=name, fuel_type=fuel_type, fuel_weight=fuel_weight, fdi=fdi, ros=ros))

    try:
        with transaction.atomic():
            FireBehaviour.objects.filter(bushfire=bushfire).delete()
            FireBehaviour.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_legal_fs(bushfire, legal_formset):
    new_fs_object = []
    for form in legal_formset:
        if form.is_valid():
            protection = form.cleaned_data.get('protection')
            cost = form.cleaned_data.get('cost')
            restricted_period = form.cleaned_data.get('restricted_period')
            prohibited_period = form.cleaned_data.get('prohibited_period')
            inv_undertaken = form.cleaned_data.get('inv_undertaken')
            legal_result = form.cleaned_data.get('legal_result')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (protection and cost and inv_undertaken and legal_result):
                new_fs_object.append(
                    Legal(bushfire=bushfire, protection=protection, cost=cost, restricted_period=restricted_period,
                        prohibited_period=prohibited_period, inv_undertaken=inv_undertaken, legal_result=legal_result
                    )
                )

    try:
        with transaction.atomic():
            Legal.objects.filter(bushfire=bushfire).delete()
            Legal.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_private_damage_fs(bushfire, private_damage_formset):
    new_fs_object = []
    for form in private_damage_formset:
        if form.is_valid():
            damage_type = form.cleaned_data.get('damage_type')
            number = form.cleaned_data.get('number')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (damage_type and number):
                new_fs_object.append(PrivateDamage(bushfire=bushfire, damage_type=damage_type, number=number))

    try:
        with transaction.atomic():
            PrivateDamage.objects.filter(bushfire=bushfire).delete()
            PrivateDamage.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_public_damage_fs(bushfire, public_damage_formset):
    new_fs_object = []
    for form in public_damage_formset:
        if form.is_valid():
            damage_type = form.cleaned_data.get('damage_type')
            fuel_type = form.cleaned_data.get('fuel_type')
            area = form.cleaned_data.get('area')
            remove = form.cleaned_data.get('DELETE')

            if not remove and (damage_type and fuel_type and area):
                new_fs_object.append(PublicDamage(bushfire=bushfire, damage_type=damage_type, fuel_type=fuel_type, area=area))

    try:
        with transaction.atomic():
            PublicDamage.objects.filter(bushfire=bushfire).delete()
            PublicDamage.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_response_fs(bushfire, response_formset):
    new_fs_object = []
    for form in response_formset:
        if form.is_valid():
            response = form.cleaned_data.get('response')
            remove = form.cleaned_data.get('DELETE')

            if not remove and response:
                new_fs_object.append(Response(bushfire=bushfire, response=response))

    try:
        with transaction.atomic():
            Response.objects.filter(bushfire=bushfire).delete()
            Response.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1

def update_comment_fs(bushfire, request, comment_formset):
    new_fs_object = []
    for form in comment_formset:
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            remove = form.cleaned_data.get('DELETE')

            if not remove and comment:
                if request.user.id:
                    new_fs_object.append(Comment(bushfire=bushfire, comment=comment, creator_id=request.user.id, modifier_id=request.user.id))
                else:
                    new_fs_object.append(Comment(bushfire=bushfire, comment=comment, creator_id=1, modifier_id=1))

    try:
        with transaction.atomic():
            Comment.objects.filter(bushfire=bushfire).delete()
            Comment.objects.bulk_create(new_fs_object)
    except IntegrityError:
        return 0

    return 1


