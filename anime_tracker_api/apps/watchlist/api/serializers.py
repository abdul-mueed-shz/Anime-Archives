from rest_framework import serializers

from apps.anime.api.serializer import AnimeSerializer
from apps.watchlist.models import WatchList, WatchlistAnime


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


class WatchlistAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchlistAnime
        fields = '__all__'


class SingleKeyListField(serializers.Field):
    def to_internal_value(self, data):
        anime_list = data.get('anime_list')
        if not isinstance(data, dict) or len(data) != 1 or not anime_list:
            raise serializers.ValidationError('Invalid data format. Must be a dictionary with a single key.')

        key = next(iter(data))
        value = data[key]

        if not isinstance(value, list):
            raise serializers.ValidationError('Invalid value. Must be a list.')

        for anime in value:
            if not isinstance(anime, dict):
                raise serializers.ValidationError('Invalid value. Anime value in list must be dict.')
            if not anime.get('id'):
                raise serializers.ValidationError('Invalid value. Anime id is mandatory.')

        return {key: value}

    def to_representation(self, value):
        return value


class AnimeListSerializer(serializers.Serializer):
    anime_list = SingleKeyListField()

    def validate_anime_list(self, value):
        key = next(iter(value))
        if not isinstance(value[key], list):
            raise serializers.ValidationError('Invalid value. Must be a list.')
        return value

    def validate(self, attrs):
        if 'anime_list' not in attrs:
            raise serializers.ValidationError('anime_list is required.')
        return attrs
