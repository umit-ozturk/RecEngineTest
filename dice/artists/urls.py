from django.urls import path

from dice.artists.views import ArtistDetailView, ArtistUpdateView

app_name = "artists"
urlpatterns = [
    path("~update/", ArtistUpdateView.as_view(), name="update"),
    path("<int:pk>/", ArtistDetailView.as_view(), name="detail"),
]
