from rest_framework import serializers

from apps.watchlist.models import WatchList


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = [
            'id',
            'user',
            'name',
            'anime_list'
        ]
