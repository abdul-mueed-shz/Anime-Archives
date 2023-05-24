from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
