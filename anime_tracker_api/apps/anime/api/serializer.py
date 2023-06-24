from rest_framework import serializers

from apps.anime.models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = [
            'id',
            'mal_id',
            'name',
            'thumbnail'
        ]
