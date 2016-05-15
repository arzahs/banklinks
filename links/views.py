from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Link
from .forms import AddLinkForm
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LinkListView(ListView):
    model = Link
    template_name = 'links/list.html'
    context_object_name = 'links'
    paginate_by = 10


class CreateLinkView(CreateView):
    form_class = AddLinkForm
    template_name = 'links/add.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateLinkView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        link = form.save(commit=False)
        link.user = self.request.user
        link.save()
        return redirect('links:list')





