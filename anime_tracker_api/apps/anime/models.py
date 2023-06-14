from django.db import models

from apps.common.models import BaseModel


class Anime(BaseModel):
    mal_id = models.IntegerField(blank=False, null=False, unique=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        db_table = 'anime'
