from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.forms.formsets import formset_factory

from bushfire.models import (Bushfire, Activity, Response, AreaBurnt, GroundForces, AerialForces,
        AttendingOrganisation, FireBehaviour, Legal, PrivateDamage, PublicDamage, Comment
    )
from bushfire.forms import (BushfireForm, ActivityFormSet, ResponseFormSet, AreaBurntFormSet,
        GroundForcesFormSet, AerialForcesFormSet, AttendingOrganisationFormSet, FireBehaviourFormSet,
        LegalFormSet, PrivateDamageFormSet, PublicDamageFormSet, CommentFormSet
    )
from bushfire.utils import breadcrumbs_li
from django.db import IntegrityError, transaction
from django.contrib import messages

class BushfireView(generic.ListView):
    model = Bushfire
    template_name = 'bushfire/bushfire.html'

#    def get_queryset(self):
#        #return Permutation.objects.all().filter(scenario__id=self.kwargs['pk'])
#        return Bushfire.objects.all()
#
#    def get_context_data(self, **kwargs):
#        context = super(BushfireView, self).get_context_data(**kwargs)
#        bushfire = Bushfire.objects.get(pk=self.kwargs['pk'])
#
#        links = [
#            (reverse('bushfire:bushfire'), 'Bushfire {}'.format(bushfire.id)),
#            (None, 'Bushfire')
#        ]
#        context['model_name'] = self.model._meta.model_name
#        context['breadcrumb_trail'] = breadcrumbs_li(links)
#
#        return context


class BushfireDetailView(generic.DetailView):
    model = Bushfire
    template_name = 'bushfire/detail.html'

    def get_context_data(self, **kwargs):
        context = super(BushfireDetailView, self).get_context_data(**kwargs)

        id = self.kwargs['pk']
        bushfire = Bushfire.objects.get(id=id)

        context.update({'bushfire': bushfire})
        return context


class BushfireCreateView(CreateView):
    model = Bushfire
    fields = ['name']
    template_name = 'bushfire/detail.html'


class _BushfireUpdateView(UpdateView):
    model = Bushfire
    #fields = ['name']
    template_name = 'bushfire/detail.html'


class BushfireUpdateView(UpdateView):
    model = Bushfire
    form_class = BushfireForm
    #template_name = 'bushfire/detail2.html'
    template_name = 'bushfire/detail4.html'
    success_url = 'success'

#    def get_form_kwargs(self):
#        # pass "user" keyword argument with the current user to your form
#        kwargs = super(BushfireCreateView2, self).get_form_kwargs()
#        kwargs['user'] = self.request.user
#        return kwargs

    def get_success_url(self):
        return reverse("bushfire:index")

    def post(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        activity_formset        = ActivityFormSet(self.request.POST, prefix='activity_fs')
#        response_formset        = ResponseFormSet(self.request.POST, prefix='response_fs')
#        area_burnt_formset      = AreaBurntFormSet(self.request.POST, prefix='area_burnt_fs')
#        groundforces_formset    = GroundForcesFormSet(self.request.POST, prefix='groundforces_fs')
#        aerialforces_formset    = AerialForcesFormSet(self.request.POST, prefix='aerialforces_fs')
#        attending_org_formset   = AttendingOrganisationFormSet(self.request.POST, prefix='attending_org_fs')
#        fire_behaviour_formset  = FireBehaviourFormSet(self.request.POST, prefix='fire_behaviour_fs')
#        legal_formset           = LegalFormSet(self.request.POST, prefix='legal_fs')
#        private_damage_formset  = PrivateDamageFormSet(self.request.POST, prefix='private_damage_fs')
#        public_damage_formset   = PublicDamageFormSet(self.request.POST, prefix='public_damage_fs')
        comment_formset         = CommentFormSet(self.request.POST, prefix='comment_fs')

        import ipdb; ipdb.set_trace()
        if form.is_valid(): # and activity_formset.is_valid():
            return self.form_valid(request,
                form,
                activity_formset,
#                response_formset,
#                area_burnt_formset,
#                groundforces_formset,
#                aerialforces_formset,
#                attending_org_formset,
#                fire_behaviour_formset,
#                legal_formset,
#                private_damage_formset,
#                public_damage_formset,
                comment_formset
            )
        else:
            return self.form_invalid(request,
                form,
                activity_formset,
#                response_formset,
#                area_burnt_formset,
#                groundforces_formset,
#                aerialforces_formset,
#                attending_org_formset,
#                fire_behaviour_formset,
#                legal_formset,
#                private_damage_formset,
#                public_damage_formset,
                comment_formset
            )

    def form_invalid(self, request,
            form,
            activity_formset,
#            response_formset,
#            area_burnt_formset,
#            groundforces_formset,
#            aerialforces_formset,
#            attending_org_formset,
#            fire_behaviour_formset,
#            legal_formset,
#            private_damage_formset,
#            public_damage_formset,
            comment_formset
        ):
        #import ipdb; ipdb.set_trace()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                activity_formset=activity_formset,
#                response_formset=response_formset,
#                area_burnt_formset=area_burnt_formset,
#                groundforces_formset=groundforces_formset,
#                aerialforces_formset=aerialforces_formset,
#                attending_org_formset=attending_org_formset,
#                fire_behaviour_formset=fire_behaviour_formset,
#                legal_formset=legal_formset,
#                private_damage_formset=private_damage_formset,
#                public_damage_formset=public_damage_formset,
                comment_formset=comment_formset,
            )
        )

    def form_valid(self, request,
            form,
            activity_formset,
#            response_formset,
#            area_burnt_formset,
#            groundforces_formset,
#            aerialforces_formset,
#            attending_org_formset,
#            fire_behaviour_formset,
#            legal_formset,
#            private_damage_formset,
#            public_damage_formset,
            comment_formset
        ):
        self.object = form.save()

        activities_updated = self.update_activity_fs(activity_formset)
#        responses_updated = self.update_response_fs(response_formset)
#        areas_burnt_updated = self.update_areas_burnt_fs(area_burnt_formset)
#        groundforces_updated = self.update_groundforces_fs(groundforces_formset)
#        aerialforces_updated = self.update_aerialforces_fs(aerialforces_formset)
#        attending_org_updated = self.update_attending_org_fs(attending_org_formset)
#        fire_behaviour_updated = self.update_fire_behaviour_fs(fire_behaviour_formset)
#        legal_updated = self.update_legal_fs(legal_formset)
#        private_damage_updated = self.update_private_damage_fs(private_damage_formset)
#        public_damage_updated = self.update_public_damage_fs(public_damage_formset)
        comment_updated = self.update_comment_fs(request, comment_formset)

        redirect_referrer =  HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if not activities_updated:
            messages.error(request, 'There was an error saving Activities.')
            return redirect_referrer

#        elif not responses_updated:
#            messages.error(request, 'There was an error saving Responses.')
#            return redirect_referrer
#
#        elif not areas_burnt_updated:
#            messages.error(request, 'There was an error saving Areas Burnt.')
#            return redirect_referrer
#
#        elif not groundforces_updated:
#            messages.error(request, 'There was an error saving Ground Forces.')
#            return redirect_referrer
#
#        elif not aerialforces_updated:
#            messages.error(request, 'There was an error saving Aerial Forces.')
#            return redirect_referrer
#
#        elif not attending_org_updated:
#            messages.error(request, 'There was an error saving Attending Organisation.')
#            return redirect_referrer
#
#        elif not fire_behaviour_updated:
#            messages.error(request, 'There was an error saving Fire Behaviour.')
#            return redirect_referrer
#
#        elif not legal_updated:
#            messages.error(request, 'There was an error saving Legal.')
#            return redirect_referrer
#
#        elif not private_damage_updated:
#            messages.error(request, 'There was an error saving Private Damage.')
#            return redirect_referrer
#
#        elif not public_damage_updated:
#            messages.error(request, 'There was an error saving Public Damage.')
#            return redirect_referrer
#
        elif not comment_updated:
            messages.error(request, 'There was an error saving Comment.')
            return redirect_referrer

        return HttpResponseRedirect(self.get_success_url())

    def update_activity_fs(self, activity_formset):
        #activity_formset.instance = self.object
        new_fs_object = []
        for form in activity_formset:
            if form.is_valid():
                activity = form.cleaned_data.get('activity')
                dt = form.cleaned_data.get('date')
                remove = form.cleaned_data.get('DELETE')

                if not remove and (activity and dt):
                    new_fs_object.append(Activity(bushfire=self.object, activity=activity, date=dt))

        try:
            with transaction.atomic():
                #Replace the old with the new
                Activity.objects.filter(bushfire=self.object).delete()
                Activity.objects.bulk_create(new_fs_object)
        except IntegrityError: #If the transaction failed
            return 0

        return 1

    def update_response_fs(self, response_formset):
        new_fs_object = []
#        response_formset.cleaned_data # hack - form.cleaned_data is unavailable unless this is called
        for form in response_formset:
            if form.is_valid():
                response = form.cleaned_data.get('response')
                remove = form.cleaned_data.get('DELETE')

                if not remove and response:
                    new_fs_object.append(Response(bushfire=self.object, response=response))

        try:
            with transaction.atomic():
                Response.objects.filter(bushfire=self.object).delete()
                Response.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_areas_burnt_fs(self, area_burnt_formset):
        new_fs_object = []
        for form in area_burnt_formset:
            if form.is_valid():
                tenure = form.cleaned_data.get('tenure')
                fuel_type = form.cleaned_data.get('fuel_type')
                area = form.cleaned_data.get('area')
                origin = form.cleaned_data.get('origin')
                remove = form.cleaned_data.get('DELETE')

                if not remove and (tenure and fuel_type and area):
                    new_fs_object.append(AreaBurnt(bushfire=self.object, tenure=tenure, fuel_type=fuel_type, area=area, origin=origin))

        try:
            with transaction.atomic():
                AreaBurnt.objects.filter(bushfire=self.object).delete()
                AreaBurnt.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_groundforces_fs(self, groundforces_formset):
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
                    new_fs_object.append(GroundForces(bushfire=self.object, name=name, persons=persons, pumpers=persons, plant=plant))

        try:
            with transaction.atomic():
                GroundForces.objects.filter(bushfire=self.object).delete()
                GroundForces.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_aerialforces_fs(self, aerialforces_formset):
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
                    new_fs_object.append(AerialForces(bushfire=self.object, name=name, observer=observer, transporter=transporter, ignition=ignition, water_bomber=water_bomber))

        try:
            with transaction.atomic():
                AerialForces.objects.filter(bushfire=self.object).delete()
                AerialForces.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_attending_org_fs(self, attending_org_formset):
        new_fs_object = []
        for form in attending_org_formset:
            if form.is_valid():
                name = form.cleaned_data.get('name')
                other = form.cleaned_data.get('other')
                remove = form.cleaned_data.get('DELETE')

                if not remove and (name and other):
                    new_fs_object.append(AttendingOrganisation(bushfire=self.object, name=name, other=other))

        try:
            with transaction.atomic():
                AttendingOrganisation.objects.filter(bushfire=self.object).delete()
                AttendingOrganisation.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_fire_behaviour_fs(self, fire_behaviour_formset):
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
                    new_fs_object.append(FireBehaviour(bushfire=self.object, name=name, fuel_type=fuel_type, fuel_weight=fuel_weight, fdi=fdi, ros=ros))

        try:
            with transaction.atomic():
                FireBehaviour.objects.filter(bushfire=self.object).delete()
                FireBehaviour.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_legal_fs(self, legal_formset):
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
                        Legal(bushfire=self.object, protection=protection, cost=cost, restricted_period=restricted_period,
                            prohibited_period=prohibited_period, inv_undertaken=inv_undertaken, legal_result=legal_result
                        )
                    )

        try:
            with transaction.atomic():
                Legal.objects.filter(bushfire=self.object).delete()
                Legal.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_private_damage_fs(self, private_damage_formset):
        new_fs_object = []
        for form in private_damage_formset:
            if form.is_valid():
                damage_type = form.cleaned_data.get('damage_type')
                number = form.cleaned_data.get('number')
                remove = form.cleaned_data.get('DELETE')

                if not remove and (damage_type and number):
                    new_fs_object.append(PrivateDamage(bushfire=self.object, damage_type=damage_type, number=number))

        try:
            with transaction.atomic():
                PrivateDamage.objects.filter(bushfire=self.object).delete()
                PrivateDamage.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_public_damage_fs(self, public_damage_formset):
        new_fs_object = []
        for form in public_damage_formset:
            if form.is_valid():
                damage_type = form.cleaned_data.get('damage_type')
                fuel_type = form.cleaned_data.get('fuel_type')
                area = form.cleaned_data.get('area')
                remove = form.cleaned_data.get('DELETE')

                if not remove and (damage_type and fuel_type and area):
                    new_fs_object.append(PublicDamage(bushfire=self.object, damage_type=damage_type, fuel_type=fuel_type, area=area))

        try:
            with transaction.atomic():
                PublicDamage.objects.filter(bushfire=self.object).delete()
                PublicDamage.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1

    def update_comment_fs(self, request, comment_formset):
        new_fs_object = []
        for form in comment_formset:
            if form.is_valid():
                comment = form.cleaned_data.get('comment')
                remove = form.cleaned_data.get('DELETE')

                if not remove and comment:
                    if request.user.id:
                        new_fs_object.append(Comment(bushfire=self.object, comment=comment, creator_id=request.user.id, modifier_id=request.user.id))
                    else:
                        new_fs_object.append(Comment(bushfire=self.object, comment=comment, creator_id=1, modifier_id=1))

        try:
            Comment.objects.filter(bushfire=self.object).delete()
            Comment.objects.bulk_create(new_fs_object)
        except IntegrityError:
            return 0

        return 1


    def get_context_data(self, **kwargs):
        context = super(BushfireUpdateView, self).get_context_data(**kwargs)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        activity_formset        = ActivityFormSet(instance=self.object, prefix='activity_fs') # self.object posts the initial data
#        response_formset        = ResponseFormSet(instance=self.object, prefix='response_fs')
#        area_burnt_formset      = AreaBurntFormSet(instance=self.object, prefix='area_burnt_fs')
#        groundforces_formset    = GroundForcesFormSet(instance=self.object, prefix='groundforces_fs')
#        aerialforces_formset    = AerialForcesFormSet(instance=self.object, prefix='aerialforces_fs')
#        attending_org_formset   = AttendingOrganisationFormSet(instance=self.object, prefix='attending_org_fs')
#        fire_behaviour_formset  = FireBehaviourFormSet(instance=self.object, prefix='fire_behaviour_fs')
#        legal_formset           = LegalFormSet(instance=self.object, prefix='legal_fs')
#        private_damage_formset  = PrivateDamageFormSet(instance=self.object, prefix='private_damage_fs')
#        public_damage_formset   = PublicDamageFormSet(instance=self.object, prefix='public_damage_fs')
        comment_formset         = CommentFormSet(instance=self.object, prefix='comment_fs')
        context.update({'form': form,
                        'activity_formset': activity_formset,
#                        'response_formset': response_formset,
#                        'area_burnt_formset': area_burnt_formset,
#                        'groundforces_formset': groundforces_formset,
#                        'aerialforces_formset': aerialforces_formset,
#                        'attending_org_formset': attending_org_formset,
#                        'fire_behaviour_formset': fire_behaviour_formset,
#                        'legal_formset': legal_formset,
#                        'private_damage_formset': private_damage_formset,
#                        'public_damage_formset': public_damage_formset,
                        'comment_formset': comment_formset,
            })
        return context



