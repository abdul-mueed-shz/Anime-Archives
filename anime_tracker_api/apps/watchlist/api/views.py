import json

from django.shortcuts import get_object_or_404
from rest_framework import exceptions, status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import WatchlistSerializer
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

    @action(methods=['post'], detail=True, url_name='add-to-watchlist', url_path='add-to-watchlist')
    def add_watchlist(self, request, pk=None):
        user_watchlist = get_object_or_404(WatchList, pk=pk)
        anime_list = request.data.get('anime_list')
        if not anime_list:
            raise exceptions.NotAcceptable
        if not user_watchlist.anime_list:
            user_watchlist.anime_list = anime_list
            user_watchlist.save()
            data = self.get_serializer(user_watchlist).data
            return Response({
                'watchlist': data,
            }, status=status.HTTP_200_OK)
        data = self.get_serializer(user_watchlist).data
        return Response({
            'watchlist': data
        })
