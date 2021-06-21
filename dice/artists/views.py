from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, UpdateView

from dice.artists.models import Artist


class ArtistListView(LoginRequiredMixin, ListView):

    model = Artist


class ArtistDetailView(LoginRequiredMixin, DetailView):

    model = Artist


class ArtistUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Artist
    fields = ["name"]
    success_message = _("Information successfully updated")
