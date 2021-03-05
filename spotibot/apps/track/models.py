import logging

from django.db import models

from spotibot.apps.album.models import Album
from spotibot.apps.artist.models import Artist
from spotibot.apps.base.models import BaseModel

logger = logging.getLogger(__name__)


class Track(BaseModel):
    class Meta:
        db_table = "models_tracks"

    name = models.CharField(max_length=100)
    popularity = models.IntegerField(default=0)
    track_number = models.IntegerField(default=0)
    uri = models.CharField(
        max_length=100,
        unique=True,
    )

    album = models.ForeignKey(Album, on_delete=models.DO_NOTHING)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    features = models.ManyToManyField(Artist, related_name="featured")

    def __str__(self):
        return f"{self.name} by {self.artist.name} ({self.album.name})"

    @classmethod
    def parse(cls, data: dict) -> "Track":
        try:
            track = Track.objects.all().get(id=data["id"])
        except Track.DoesNotExist:
            artist, *features = data["artists"]

            track = Track(
                id=data["id"],
                name=data["name"],
                popularity=data.get("popularity", 0),
                track_number=data.get("track_number", 0),
                uri=data["uri"],
                artist=Artist.parse(artist),
                album=Album.parse(data["album"]),
            )
            track.save()

            logger.info("Added new track: %s", track)

            for feature in features:
                track.features.add(Artist.parse(feature))

        track.popularity = data.get("popularity", 0)
        track.save()

        return track
