from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.forms.formsets import formset_factory

from bushfire.models import Bushfire
from bushfire.forms import BushfireForm, ActivityFormSet
from bushfire.utils import breadcrumbs_li

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
    template_name = 'bushfire/detail2.html'
    success_url = 'success'

#    def get_form_kwargs(self):
#        # pass "user" keyword argument with the current user to your form
#        kwargs = super(BushfireCreateView2, self).get_form_kwargs()
#        kwargs['user'] = self.request.user
#        return kwargs

    def get_success_url(self):
        return reverse("bushfire:index")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        activity_formset = ActivityFormSet(self.request.POST)

        import ipdb; ipdb.set_trace()
        if form.is_valid() and activity_formset.is_valid():
            return self.form_valid(form, activity_formset)
        else:
            return self.form_invalid(form, activity_formset)



#    def post(self, request, *args, **kwargs):
#        super(BushfireCreateView2, self).post(request, *args, **kwargs)
#        self.object.save()
#        return HttpResponseRedirect(self.get_success_url())

#    def get_object(self, queryset=None):
#        return super(BushfireCreateView2, self).get_object()

    def form_invalid(self, form, activity_formset):
        import ipdb; ipdb.set_trace()
        #return super(BushfireCreateView2, self).form_invalid(form)
        return self.render_to_response(
            self.get_context_data(form=form, activity_formset=activity_formset)
        )

    def form_valid(self, form, activity_formset):
        import ipdb; ipdb.set_trace()
        self.object = form.save()
        activity_formset.instance = self.object
        activity_formset.save()
        return HttpResponseRedirect(self.get_success_url())
        #return super(BushfireCreateView2, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BushfireUpdateView, self).get_context_data(**kwargs)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #ActivityFormSet = formset_factory(ActivityForm, max_num=7)
        activity_formset = ActivityFormSet()
        context.update({'form': form, 'activity_formset': activity_formset, 'myval': 'MyVal'})
        return context


