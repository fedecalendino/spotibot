import logging
from typing import Iterable
from pathlib import Path

from django.conf import settings
from spotipy import Spotify, CacheFileHandler
from spotipy.oauth2 import SpotifyOAuth

from . import util

logger = logging.getLogger(__name__)


client = Spotify(
    auth_manager=SpotifyOAuth(
        username=settings.SPOTIFY["USERNAME"],
        client_id=settings.SPOTIFY["CLIENT_ID"],
        client_secret=settings.SPOTIFY["CLIENT_SECRET"],
        scope="playlist-modify-public,playlist-modify-private,user-library-read,user-read-recently-played",
        redirect_uri="https://localhost:8080",
        cache_handler=CacheFileHandler(cache_path=str(Path.home() / ".spotify"))
    )
)


def get_user_history():
    return client.current_user_recently_played()


def get_user_saved_tracks(limit: int = 10):
    return client.current_user_saved_tracks(limit=limit)


def change_playlist_details(playlist_id: str, description: str):
    client.playlist_change_details(playlist_id, description=description)


def clear_playlist(playlist_id: str):
    client.playlist_replace_items(playlist_id, items=[])
    logger.info("Cleared playlist %s", playlist_id)


def update_playlist(playlist_id: str, items: Iterable[str], clear: bool = True):
    if clear:
        clear_playlist(playlist_id)

    for chunk in util.chunks(list(items), size=50):
        client.playlist_add_items(playlist_id, items=chunk)
        logger.info("Added %i tracks to playlist %s", len(chunk), playlist_id)
