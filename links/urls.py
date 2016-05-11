from django.conf.urls import url, include
from .views import LinkListView


urlpatterns = [
   url(r'^list/', LinkListView.as_view(), name='list'),
]
