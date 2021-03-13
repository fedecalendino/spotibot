import logging

from django.db import models

from spotibot.apps.artist.models import Artist
from spotibot.apps.base.models import BaseModel
from spotibot.spotify.api import client

logger = logging.getLogger(__name__)


class Album(BaseModel):
    class Meta:
        db_table = "albums"

    name = models.TextField()
    uri = models.CharField(max_length=100, unique=True)

    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)

    @property
    def tracks(self):
        from spotibot.apps.track.models import Track

        ids = list(
            map(lambda track: track["id"], client.album_tracks(self.id)["items"]),
        )

        return sorted(
            list(map(Track.parse, client.tracks(ids)["tracks"])),
            key=lambda track: track.number,
        )

    def __str__(self):
        return f"{self.name} by {self.artist.name}"

    @classmethod
    def parse(cls, data: dict) -> "Album":
        try:
            album = Album.objects.all().get(id=data["id"])
        except Album.DoesNotExist:
            album = Album(
                id=data["id"],
                name=data["name"],
                uri=data["uri"],
                artist=Artist.parse(data["artists"][0]),
            )
            album.save()

            logger.info("Added new album: %s", album)

        return album
