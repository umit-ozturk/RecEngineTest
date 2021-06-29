from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from dice.recommendations.api.serializers import RecommendationSerializer
from dice.recommendations.models import Recommendation
from dice.recommendations.tasks import (
    recommend_closest_artist,
    recommend_closest_per_cluster,
)


class RecommendationViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()
    lookup_field = "id"

    @action(
        detail=False,
        methods=["post"],
        url_path="recommend-close-artist",
        url_name="recommend-artist-close-artist",
    )
    def recommend_artist_close_artist(self, request):
        """
        Endpoint recommends artists for user
        """
        try:
            data = request.data
            serializer = RecommendationSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            recommendation = serializer.save()
            recommend_closest_artist.delay(
                recommendation.id,
                recommendation.count,
                recommendation.user.embedding,
            )

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                data={"error_message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        detail=False,
        methods=["post"],
        url_path="recommend-per-cluster",
        url_name="recommend-artist-per-cluster",
    )
    def recommend_artist_per_cluster(self, request):
        """
        Endpoint recommends artists for user per cluster.
        """
        try:
            data = request.data
            serializer = RecommendationSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            recommendation = serializer.save()
            recommend_closest_per_cluster.delay(
                recommendation.id,
                recommendation.count,
                recommendation.user.embedding,
            )

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                data={"error_message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
