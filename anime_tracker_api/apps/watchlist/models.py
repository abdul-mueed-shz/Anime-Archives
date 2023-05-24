from django.contrib.auth.models import User
from django.db import models

from apps.common.models import BaseModel


class WatchList(BaseModel):
    user = models.ForeignKey(User, related_name='watchlist', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    anime_list = models.TextField(max_length=600, null=True, blank=True)
