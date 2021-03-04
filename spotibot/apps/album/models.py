from django.db import models

from spotibot.apps.base.models import BaseModel
from spotibot.apps.artist.models import Artist


class Album(BaseModel):
    class Meta:
        db_table = "models_albums"

    name = models.CharField(max_length=100)
    uri = models.CharField(
        max_length=100,
        unique=True,
    )

    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} ({self.id})"
