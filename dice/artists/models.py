from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Artist(models.Model):
    """
    Artist model provides the artist information for system.
    """

    name = models.CharField(
        _("Artist of name"), null=True, blank=True, max_length=255
    )

    embedding = models.JSONField(_("Artist Embedding"), blank=True, null=True)

    image_url = models.URLField(_("Artist Image Url"), null=True, blank=True)

    def get_absolute_url(self):
        """Get url for artist's detail view.

        Returns:
            str: URL for artist detail.

        """
        return reverse("artists:detail", args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
