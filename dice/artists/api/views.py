import json

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from dice.artists.api.serializers import ArtistSerializer
from dice.artists.models import Artist

User = get_user_model()


class ArtistViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    lookup_field = "id"

    @action(
        detail=False,
        methods=["get"],
        url_path="list-all-interested-users",
        url_name="all-interested-users",
    )
    def list_artists_for_user(self, request):
        """
        Endpoint lists artists for an user
        """
        try:
            artist_id = request.GET.get("artist_id", None)
            if artist_id:
                interested_users = set()

                for user in User.objects.all():
                    if int(artist_id) in user.combined_recommendations:
                        if user.id:
                            interested_users.add(user.id)

                return Response(
                    data=json.dumps({"users": list(interested_users)}),
                    status=status.HTTP_200_OK,
                )
            return Response(
                data={"error_message": "artist_id couldn't find."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                data={"error_message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
