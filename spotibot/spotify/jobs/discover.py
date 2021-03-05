import logging

from django.conf import settings

from spotibot.apps.track.models import Track
from spotibot.spotify import api
from spotibot.spotify import util

logger = logging.getLogger(__name__)


DISCOVER_PLAYLIST_ID = settings.SPOTIFY["PLAYLISTS"]["DISCOVER"]


def run() -> list[Track]:
    tracks = []

    for data in api.get_user_saved_tracks(limit=10)["items"]:
        track = Track.parse(data["track"])
        tracks.append(track)

    api.update_playlist(
        DISCOVER_PLAYLIST_ID,
        items=map(lambda item: item.uri, tracks),
        clear=True,
    )

    api.change_playlist_details(
        DISCOVER_PLAYLIST_ID,
        description=f"{'; '.join(map(lambda item: item.name, tracks))}. Updated at {util.timestamp()}",
    )

    return tracks
