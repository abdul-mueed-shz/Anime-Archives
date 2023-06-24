from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.anime.api.serializer import AnimeSerializer
from apps.anime.models import Anime


# Create your views here.
class AnimeViewSet(ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    http_method_names = [
        'get',
        'post',
        'delete',
        'put',
        'patch'
    ]

    def create(self, request, *args, **kwargs):
        """
        Create method overridden to handle duplicate anime creation error.
        @param request: The HTTP request object.
        @type request: rest_framework.request.Request
        @param args: Additional positional arguments.
        @param kwargs: Additional keyword arguments.
        @return: The response containing the created anime or error message.
        @rtype: rest_framework.response.Response
        """
        try:
            response = super().create(request, *args, **kwargs)
        except ValidationError as e:
            error_detail = e.detail
            if 'mal_id' in error_detail and 'anime with this mal id already exists.' in error_detail['mal_id']:
                anime = Anime.objects.get(mal_id=request.data.get('mal_id'))
                anime_data = AnimeSerializer(anime).data
                return Response({
                    **anime_data,
                    'message': 'Anime with this mal id already exists'
                })
        return response
