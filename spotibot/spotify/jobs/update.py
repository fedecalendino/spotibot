import logging
from time import sleep

from spotibot.apps.track.models import Track
from spotibot.spotify import api
from spotibot.apps.history.models import History

logger = logging.getLogger(__name__)


def run():
    total = 0

    # for index, track in enumerate(Track.objects.all()):
    #     if track.duration:
    #         total += track.duration
    #         continue
    #
    #     logger.info(f"{index} > Fetching {track}...")
    #     data = api.client.track(track.id)
    #
    #     track.duration = data.get("duration_ms", 0)
    #     track.save()
    #
    #     total += track.duration
    #
    #     sleep(0.1)

    for item in History.objects.all():
        total += item.track.duration

    logger.info(f"{total} ms")
    logger.info(f"{total/1000} s")
    logger.info(f"{total / 1000 / 60} m")
    logger.info(f"{total / 1000 / 60 / 60} h")
    logger.info(f"{total / 1000 / 60 / 60 / 24} d")
