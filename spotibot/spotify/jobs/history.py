import logging
from typing import List

from django.conf import settings

from spotibot.apps.history.models import History
from spotibot.spotify import api
from spotibot.spotify import util


logger = logging.getLogger(__name__)


HISTORY_PLAYLIST_ID = settings.SPOTIFY["PLAYLISTS"]["HISTORY"]


def run() -> List[History]:
    items = []

    for data in api.get_user_history()["items"]:
        history = History.parse(data)
        items.append(history)

    api.update_playlist(
        HISTORY_PLAYLIST_ID,
        items=map(lambda item: item.track.uri, items),
    )

    api.change_playlist_details(
        HISTORY_PLAYLIST_ID,
        description=f"Last 50 songs played. Updated at {util.timestamp()}",
    )

    return items
