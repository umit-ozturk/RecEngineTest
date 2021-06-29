import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


def generate_custom_user_pk():
    """
    Generate custom user pk for User Model.
    Note: Just for exercise because of that
    "Primary key is already in the database" issue didn't check.

    :return: UUID as hex
    """
    return uuid.uuid4().hex


class User(AbstractUser):
    """Default user for Dice."""

    id = models.CharField(
        _("ID"),
        primary_key=True,
        default=generate_custom_user_pk,
        max_length=255,
    )
    embedding = models.JSONField(_("User Embedding"), blank=True, null=True)

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    @cached_property
    def combined_recommendations(self):
        rec_queryset = self.recommendation.values_list("recommends", flat=True)
        if not rec_queryset:
            return self.recommendation.all()  # Will return None
        rec_set = set()
        for rec in rec_queryset:
            if rec:
                rec_set.update(rec["recommendations"])
        return list(rec_set)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
