import ast
import json

from django.shortcuts import get_object_or_404
from rest_framework import exceptions, status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import WatchlistSerializer, AnimeListSerializer
from ..models import WatchList


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

    def validate_list(self, request):
        AnimeListSerializer(data=request.data).is_valid(raise_exception=True)

    @action(methods=['post'], detail=True, url_name='add-to-watchlist', url_path='add-to-watchlist')
    def add_watchlist(self, request, pk=None):
        def add_anime_to_list(data, anime_list_dict):
            anime_list = anime_list_dict.get('anime_list')
            for anime in data:
                if anime not in anime_list:
                    anime_list.append(anime)

        user_watchlist = get_object_or_404(WatchList, pk=pk)
        anime_data_dict = request.data.get('data')
        if not anime_data_dict:
            raise exceptions.NotAcceptable
        if not user_watchlist.anime_list:
            self.validate_list(request)
            user_watchlist.anime_list = anime_data_dict
            user_watchlist.save()
            data = self.get_serializer(user_watchlist).data
            data['anime_list'] = anime_data_dict
            return Response({
                'watchlist': data,
            }, status=status.HTTP_200_OK)
        self.validate_list(request)
        watchlist_obj_anime_list = ast.literal_eval(user_watchlist.anime_list)
        add_anime_to_list(anime_data_dict.get('anime_list'), watchlist_obj_anime_list)
        user_watchlist.anime_list = watchlist_obj_anime_list
        user_watchlist.save()
        data = self.get_serializer(user_watchlist).data
        data['anime_list'] = watchlist_obj_anime_list
        return Response({
            'watchlist': data
        })
