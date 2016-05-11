from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from tagging.models import Tag


class Link(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    link = models.CharField(_("Ссылка"), max_length=255)
    comment = models.TextField(_("Комментарий"), blank=True)
    date = models.DateTimeField(_("Дата содания"), auto_now=True)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return self.link

    class Meta:
        verbose_name = _("Ccылка")
        verbose_name_plural = _("Ccылки")
