import ast
import json

from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import exceptions, status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import WatchlistSerializer, AnimeListSerializer, WatchlistAnimeSerializer
from ..models import WatchList, WatchlistAnime
from ...anime.models import Anime


class WatchlistAnimeViewSet(ModelViewSet):
    queryset = WatchlistAnime.objects.all()
    serializer_class = WatchlistAnimeSerializer
    http_method_names = [
        'get',
        'post',
        'delete',
        'put',
        'patch'
    ]


class WatchListViewSet(ModelViewSet):
    serializer_class = WatchlistSerializer
    http_method_names = [
        'get',
        'post',
        'delete',
        'put',
        'patch'
    ]
    queryset = WatchList.objects.all()

    @staticmethod
    def validate_list(req):
        try:
            AnimeListSerializer(data=req).is_valid(raise_exception=True)
        except Exception as e:
            raise exceptions.ValidationError(e)
        return True

    @action(methods=['get'], detail=False, url_path='get-playlists')
    def get_watchlist_for_user(self, request):
        watchlists_objs = WatchList.objects.filter(user=request.user)
        watchlists = []
        for watchlist in watchlists_objs:
            serializer = WatchlistSerializer(watchlist)
            watchlist_data = serializer.data
            watchlist_anime_objs = WatchlistAnime.objects.filter(watchlist=watchlist)
            anime_list_serializer = WatchlistAnimeSerializer(watchlist_anime_objs, many=True)
            watchlist_data['anime_list'] = anime_list_serializer.data
            watchlists.append(watchlist_data)
        return Response(watchlists, status=status.HTTP_200_OK)

    @staticmethod
    def check_records(anime_list):
        # query = Q()
        for anime in anime_list:
            if not isinstance(anime, dict):
                raise exceptions.NotAcceptable(f'Expected a dict but got {str(type(anime))}')
            anime_id = anime.get('id')
            if not anime_id:
                raise exceptions.NotAcceptable('Anime id is required')
            if not Anime.objects.filter(id=anime_id).exists():
                return False
            # query &= Q(id=anime_id)
        return True
        # return Anime.objects.filter(query).exists()

    @staticmethod
    def add_to_watchlist_anime(watchlist_id, anime_list):
        for anime in anime_list:
            anime_data = {
                "anime": anime.get('id'),
                "watchlist": watchlist_id,
            }
            rating = anime.get('rating')
            review = anime.get('review')
            if rating:
                if not isinstance(rating, int):
                    raise exceptions.NotAcceptable('Rating must be a number less than or equal to 10')
                anime_data['rating'] = rating
            if review:
                if not isinstance(review, str):
                    raise exceptions.NotAcceptable('review must be a string')
                anime_data['review'] = review
            serializer = WatchlistAnimeSerializer(data=anime_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request.data['user'] = str(request.user.id)
        anime_list = request.data.get('anime_list')
        if anime_list:
            if not isinstance(anime_list, list):
                raise exceptions.NotAcceptable(f'Expected a list but got {str(type(anime_list))}')
            if not self.check_records(anime_list):
                raise exceptions.NotAcceptable('Incorrect anime id passed')
        watchlist = super().create(request, *args, **kwargs)
        if anime_list:
            watchlist_id = watchlist.data.get('id')
            self.add_to_watchlist_anime(watchlist_id, anime_list)
        return watchlist

    @transaction.atomic
    @action(methods=['post'], detail=True, url_name='add-to-watchlist', url_path='add-to-watchlist')
    def add_anime_to_watchlist(self, request, pk=None):
        anime_list = request.data.get('anime_list')
        if not isinstance(anime_list, list):
            raise exceptions.NotAcceptable(f'Expected a list but got {str(type(anime_list))}')
        if not self.check_records(anime_list):
            raise exceptions.NotAcceptable('Incorrect anime id passed')
        self.add_to_watchlist_anime(pk, anime_list)
        return Response({"message": "Successfully added the anime"}, status=status.HTTP_200_OK)
