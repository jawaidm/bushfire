from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.forms.formsets import formset_factory

from bushfire.models import Bushfire
from bushfire.forms import BushfireForm, ActivityForm
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


class BushfireUpdateView(UpdateView):
    model = Bushfire
    #fields = ['name']
    template_name = 'bushfire/detail.html'


class BushfireCreateView2(UpdateView):
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

#    def post(self, request, *args, **kwargs):
#        super(BushfireCreateView2, self).post(request, *args, **kwargs)
#        self.object.save()
#        return HttpResponseRedirect(self.get_success_url())

#    def get_object(self, queryset=None):
#        return super(BushfireCreateView2, self).get_object()

    def form_invalid(self, form):
        return super(BushfireCreateView2, self).form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BushfireCreateView2, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BushfireCreateView2, self).get_context_data(**kwargs)

        ActivityFormSet = formset_factory(ActivityForm)
        activity_formset = ActivityFormSet()
        context.update({'activity_formset': activity_formset, 'myval': 'MyVal'})
        return context


