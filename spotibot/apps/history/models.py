from uuid import uuid4

from django.db import models

from spotibot.apps.base.models import BaseModel
from spotibot.apps.track.models import Track


class History(BaseModel):
    class Meta:
        db_table = "history"

    played_at = models.DateTimeField(unique=True)
    raw = models.JSONField()

    track = models.ForeignKey(Track, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.track} @ {self.played_at}"

    @classmethod
    def parse(cls, data: dict) -> "History":
        try:
            history = History.objects.get(
                played_at=data["played_at"],
            )
        except History.DoesNotExist:
            history = History(
                id=str(uuid4()),
                played_at=data["played_at"],
                raw=data,
                track=Track.parse(data["track"]),
            )
            history.save()

        return history
