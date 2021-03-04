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
        username=settings.SPOTIPY["USERNAME"],
        client_id=settings.SPOTIPY["CLIENT_ID"],
        client_secret=settings.SPOTIPY["CLIENT_SECRET"],
        scope=",".join(scopes),
        redirect_uri="https://localhost:8080",
    )
)


def get_history():
    return client.current_user_recently_played()


def get_saved_tracks(limit: int = 10):
    return client.current_user_saved_tracks(limit=limit)


def clear_playlist(playlist_id: str):
    client.playlist_replace_items(
        playlist_id=playlist_id,
        items=[]
    )


def update_playlist(playlist_id: str, items: list[str]):
    client.playlist_add_items(
        playlist_id=playlist_id,
        items=items
    )
