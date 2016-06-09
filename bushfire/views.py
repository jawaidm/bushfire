from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from bushfire.models import Bushfire
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

#    def get_context_data(self, **kwargs):
#        context = super(BushfireCreateView, self).get_context_data(**kwargs)
#
#        id = self.kwargs['pk']
#        bushfire = Bushfire.objects.get(id=id)
#
#        context.update({'bushfire': bushfire})
#        return context
#

