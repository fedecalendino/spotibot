import logging
from typing import List

from django.conf import settings

from spotibot.apps.track.models import Track
from spotibot.spotify import api
from spotibot.spotify import util


logger = logging.getLogger(__name__)


DISCOVER_PLAYLIST_ID = settings.SPOTIFY["PLAYLISTS"]["DISCOVER"]


def run() -> List[Track]:
    tracks = {}

    for data in api.get_user_saved_tracks(limit=10)["items"]:
        track = Track.parse(data["track"])
        tracks[track.id] = track

    for track_id, track in list(tracks.items()):
        for artist_track in track.artist.top_tracks[:5]:
            tracks[artist_track.id] = artist_track

    for track_id, track in list(tracks.items()):
        for featured in track.features.all():
            for featured_track in featured.top_tracks[:3]:
                tracks[featured_track.id] = featured_track

    for track_id, track in list(tracks.items()):
        for featured in track.features.all():
            for featured_track in featured.top_tracks[:1]:
                tracks[featured_track.id] = featured_track

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
