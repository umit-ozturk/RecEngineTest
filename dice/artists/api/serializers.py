from rest_framework import serializers

from dice.artists.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            "name",
            "image_url",
            "embedding",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:artist-detail", "lookup_field": "id"}
        }
