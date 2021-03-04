from django.db import models

from spotibot.apps.base.models import BaseModel
from spotibot.apps.album.models import Album
from spotibot.apps.artist.models import Artist


class Track(BaseModel):
    class Meta:
        db_table = "models_tracks"

    name = models.CharField(max_length=100)
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
        artist, *features = data["artists"]

        track, _ = Track.objects.all().get_or_create(
            id=data["id"],
            name=data["name"],
            uri=data["uri"],
            artist=Artist.parse(artist),
            album=Album.parse(data["album"]),
        )

        for feature in features:
            track.features.add(Artist.parse(feature))

        track.save()

        return track
