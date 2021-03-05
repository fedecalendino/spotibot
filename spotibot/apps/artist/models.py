import logging

from django.db import models

from spotibot.apps.base.models import BaseModel

logger = logging.getLogger(__name__)


class Artist(BaseModel):
    class Meta:
        db_table = "models_artists"

    name = models.CharField(max_length=100)
    uri = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def parse(cls, data: dict) -> "Artist":
        try:
            artist = Artist.objects.all().get(id=data["id"])
        except Artist.DoesNotExist:
            artist = Artist(
                id=data["id"],
                name=data["name"],
                uri=data["uri"],
            )
            artist.save()

            logger.info("Added new artist: %s", artist)

        return artist
