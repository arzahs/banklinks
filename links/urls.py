from django.conf.urls import url, include
from .views import *


urlpatterns = [
   url(r'^list/$', LinkListView.as_view(), name='list'),
   url(r'^add/$', CreateLinkView.as_view(), name='add')
]
