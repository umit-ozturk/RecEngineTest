from django.contrib.auth import forms as admin_forms

from dice.artists.models import Artist


class ArtistChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = Artist


class ArtistCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = Artist
