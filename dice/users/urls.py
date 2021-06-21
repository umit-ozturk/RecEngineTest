from django.urls import path

from dice.users.views import UserDetailView, UserRedirectView, UserUpdateView

app_name = "users"
urlpatterns = [
    path("~redirect/", UserRedirectView.as_view(), name="redirect"),
    path("~update/", UserUpdateView.as_view(), name="update"),
    path("<str:username>/", UserDetailView.as_view(), name="detail"),
]
