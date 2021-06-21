from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from dice.artists.api.serializers import ArtistSerializer
from dice.artists.models import Artist


class ArtistViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)
