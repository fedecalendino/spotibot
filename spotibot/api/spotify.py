from typing import Iterable

from django.conf import settings
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


scopes = [
    "playlist-modify-private",
    "playlist-modify-public",
    "user-library-read",
    "user-read-recently-played",
]


client = Spotify(
    auth_manager=SpotifyOAuth(
        username=settings.SPOTIFY["USERNAME"],
        client_id=settings.SPOTIFY["CLIENT_ID"],
        client_secret=settings.SPOTIFY["CLIENT_SECRET"],
        scope=",".join(scopes),
        redirect_uri="https://localhost:8080",
    )
)


def get_history():
    return client.current_user_recently_played()


def get_saved_tracks(limit: int = 10):
    return client.current_user_saved_tracks(limit=limit)


def change_playlist_details(playlist_id: str, description: str):
    client.playlist_change_details(playlist_id, description=description)


def clear_playlist(playlist_id: str):
    replace_playlist(playlist_id, items=[])


def replace_playlist(playlist_id: str, items: Iterable[str]):
    client.playlist_replace_items(playlist_id, items=list(items))


def update_playlist(playlist_id: str, items: Iterable[str]):
    client.playlist_add_items(playlist_id, items=list(items))
