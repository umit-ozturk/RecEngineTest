from django.db import models
from django.utils.translation import gettext_lazy as _


class Recommendation(models.Model):
    """
    Recommendation model stores the recommendations.
    """

    user = models.ForeignKey(
        "users.User",
        blank=True,
        related_name="recommendation",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )

    count = models.PositiveSmallIntegerField(
        _("Recommendation Counts"), default=5
    )

    recommends = models.JSONField(
        _("User Recommendations"), blank=True, null=True
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Recommendation")
        verbose_name_plural = _("Recommendations")
