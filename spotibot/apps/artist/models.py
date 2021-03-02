from django.db import models
from spotibot.apps.base.models import BaseModel


class Artist(BaseModel):
    class Meta:
        db_table = "models_artists"

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.id})"
