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

    @staticmethod
    def validate_list(req):
        try:
            AnimeListSerializer(data=req).is_valid(raise_exception=True)
        except Exception as e:
            raise exceptions.ValidationError(e)
        return True

    @action(methods=['get'], detail=False, url_path='get-playlists')
    def get_watchlist_for_user(self, request):
        watchlists_obj = WatchList.objects.filter(user=request.user)
        serializer = WatchlistSerializer(watchlists_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        anime_list = request.data.get('anime_list')
        request.data['user'] = str(request.user.id)
        if anime_list:
            self.validate_list(request.data)
            request.data['anime_list'] = str(anime_list)
        response = super().create(request, *args, **kwargs)
        response.data["anime_list"] = anime_list
        return response

    @action(methods=['post'], detail=True, url_name='add-to-watchlist', url_path='add-to-watchlist')
    def add_watchlist(self, request, pk=None):

        def add_anime_to_list(anime_data, anime_list_dict):
            anime_list = anime_list_dict.get('anime_list')
            for anime in anime_data:
                if anime not in anime_list:
                    anime_list.append(anime)

        user_watchlist = get_object_or_404(WatchList, pk=pk, user=request.user)
        anime_data_dict = request.data.get('anime_list')
        if not anime_data_dict:
            raise exceptions.NotAcceptable
        if not user_watchlist.anime_list:
            self.validate_list(request.data)
            user_watchlist.anime_list = anime_data_dict
            user_watchlist.save()
            data = self.get_serializer(user_watchlist).data
            data['anime_list'] = anime_data_dict
            return Response({
                'watchlist': data,
            }, status=status.HTTP_200_OK)
        self.validate_list(request.data)
        watchlist_obj_anime_list = ast.literal_eval(user_watchlist.anime_list)
        add_anime_to_list(anime_data_dict.get('anime_list'), watchlist_obj_anime_list)
        user_watchlist.anime_list = watchlist_obj_anime_list
        user_watchlist.save()
        data = self.get_serializer(user_watchlist).data
        data['anime_list'] = watchlist_obj_anime_list
        return Response({
            'watchlist': data
        })
