import logging

from django.conf import settings

from spotibot.apps.track.models import Track
from spotibot.spotify import api
from spotibot.spotify import util

logger = logging.getLogger(__name__)


DISCOVER_PLAYLIST_ID = settings.SPOTIFY["PLAYLISTS"]["DISCOVER"]


def run() -> list[Track]:
    artists = []
    tracks = {}

    for data in api.get_user_saved_tracks(limit=10)["items"]:
        track = Track.parse(data["track"])
        tracks[track.id] = track

        artists.append(track.artist)

        album_tracks = sorted(
            track.album.tracks,
            key=lambda tr: tr.popularity,
            reverse=True,
        )

        for album_track in album_tracks[:3]:
            tracks[album_track.id] = album_track

    api.update_playlist(
        DISCOVER_PLAYLIST_ID,
        items=tracks.keys(),
        clear=True,
    )

    api.change_playlist_details(
        DISCOVER_PLAYLIST_ID,
        description=f"Discover new songs based on liked songs. Updated at {util.timestamp()}",
    )

    return tracks.values()
