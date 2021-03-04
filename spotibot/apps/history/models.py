from django.db import models

from spotibot.apps.base.models import BaseModel
from spotibot.apps.track.models import Track


class History(BaseModel):
    class Meta:
        db_table = "models_history"

    played_at = models.DateTimeField(unique=True)
    track = models.ForeignKey(Track, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.track.title} @ {self.played_at}"
