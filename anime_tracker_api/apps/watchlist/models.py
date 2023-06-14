from django.db import models

from apps.anime.models import Anime
from apps.common.models import BaseModel
from apps.user.models import User


class WatchList(BaseModel):
    user = models.ForeignKey(User, related_name='watchlist', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)


class WatchlistAnime(BaseModel):
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.PROTECT)
    rating = models.IntegerField(max_length=10, default=0)
    review = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        unique_together = ["watchlist", "anime"]
