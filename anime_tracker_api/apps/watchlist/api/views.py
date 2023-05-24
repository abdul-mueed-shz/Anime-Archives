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

    def create(self, request, *args, **kwargs):
        return Response(status=200, data={
            'Status': 'Under production'
        })
