from django.urls import path

from dice.artists.views import (
    ArtistDetailView,
    ArtistListView,
    ArtistUpdateView,
)

app_name = "artists"

urlpatterns = [
    path("list/", ArtistListView.as_view(), name="list"),
    path("~update/", ArtistUpdateView.as_view(), name="update"),
    path("<int:pk>/", ArtistDetailView.as_view(), name="detail"),
]
