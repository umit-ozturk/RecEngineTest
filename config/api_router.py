from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from dice.artists.api.views import ArtistViewSet
from dice.recommendations.api.views import RecommendationViewSet
from dice.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("artists", ArtistViewSet)
router.register("recommendations", RecommendationViewSet)


app_name = "api"
urlpatterns = router.urls
