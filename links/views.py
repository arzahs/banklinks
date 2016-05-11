from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Link


class LinkListView(ListView):
    model = Link
    template_name = 'links/list.html'
    context_object_name = 'links'


