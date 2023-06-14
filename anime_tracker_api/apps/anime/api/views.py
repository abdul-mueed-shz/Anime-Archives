from rest_framework.viewsets import ModelViewSet

from apps.anime.api.serializer import AnimeSerializer
from apps.anime.models import Anime


# Create your views here.
class AnimeViewSet(ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
