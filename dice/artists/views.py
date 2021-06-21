from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, UpdateView

from dice.artists.models import Artist


class ArtistDetailView(LoginRequiredMixin, DetailView):

    model = Artist


class ArtistUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Artist
    fields = ["name"]
    success_message = _("Information successfully updated")
