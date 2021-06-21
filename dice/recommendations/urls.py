from django.urls import path

from dice.recommendations.views import (
    RecommendationCreateView,
    RecommendationListView,
)

app_name = "recommendations"

urlpatterns = [
    path("", RecommendationListView.as_view(), name="list"),
    path("create/", RecommendationCreateView.as_view(), name="create"),
]
