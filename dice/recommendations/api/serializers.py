from rest_framework import serializers

from dice.recommendations.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ["id", "user", "method", "count", "recommends"]
