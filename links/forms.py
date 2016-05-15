from django.forms import Form, ModelForm
from .models import Link


class AddLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['link', 'comment', 'tags']


