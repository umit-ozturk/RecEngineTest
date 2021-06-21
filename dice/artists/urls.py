from django.urls import path

from dice.artists.views import (
    ArtistDetailView,
    ArtistListView,
    ArtistUpdateView,
)

app_name = "artists"

urlpatterns = [
    path("", ArtistListView.as_view(), name="list"),
    path("<int:pk>/update/", ArtistUpdateView.as_view(), name="update"),
    path("<int:pk>/", ArtistDetailView.as_view(), name="detail"),
]
