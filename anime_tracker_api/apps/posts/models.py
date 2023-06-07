from django.db import models

from apps.common.models import BaseModel
from apps.user.models import User

STATUS = (
    (0, "DRAFT"),
    (1, "PUBLISH"),
    (2, "ARCHIVE"),
)


# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
