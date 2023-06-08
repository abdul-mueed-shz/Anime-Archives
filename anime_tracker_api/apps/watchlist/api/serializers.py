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


class SingleKeyListField(serializers.Field):
    def to_internal_value(self, data):
        anime_list = data.get('anime_list')
        if not isinstance(data, dict) or len(data) != 1 or not anime_list:
            raise serializers.ValidationError('Invalid data format. Must be a dictionary with a single key.')

        key = next(iter(data))
        value = data[key]

        if not isinstance(value, list):
            raise serializers.ValidationError('Invalid value. Must be a list.')

        return {key: value}

    def to_representation(self, value):
        return value


class AnimeListSerializer(serializers.Serializer):
    data = SingleKeyListField()

    def validate_data(self, value):
        key = next(iter(value))
        if not isinstance(value[key], list):
            raise serializers.ValidationError('Invalid value. Must be a list.')
        return value

    def validate(self, attrs):
        if 'data' not in attrs:
            raise serializers.ValidationError('anime_list is required.')
        return attrs
