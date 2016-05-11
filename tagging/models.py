from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Tag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(_('Название'), max_length=25)
    description = models.TextField(_("Описание"))

    class Meta:
        verbose_name = _("Тег")
        verbose_name_plural = _("Теги")


