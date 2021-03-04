from django.db import models

from spotibot.apps.base.models import BaseModel


class Artist(BaseModel):
    class Meta:
        db_table = "models_artists"

    name = models.CharField(max_length=100)
    uri = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

    @classmethod
    def parse(cls, data: dict) -> "Artist":
        artist, _ = Artist.objects.all().get_or_create(
            id=data["id"],
            name=data["name"],
            uri=data["uri"],
        )
        artist.save()

        return artist
