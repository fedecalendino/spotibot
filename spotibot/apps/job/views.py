import logging

from django.http.response import JsonResponse
from django.conf import settings
from rest_framework.generics import GenericAPIView

from spotibot.api import spotify
from spotibot.apps.history.models import History
from spotibot.util import timestamp

logger = logging.getLogger(__name__)


HISTORY_PLAYLIST_ID = settings.SPOTIFY["PLAYLISTS"]["HISTORY"]


class DiscoverJobView(GenericAPIView):
    def get(self, _):
        pass


class HistoryJobView(GenericAPIView):
    def get(self, _):
        tracks = []

        for data in spotify.get_history()["items"]:
            history = History.parse(data)
            tracks.append(history.track)

        spotify.replace_playlist(
            HISTORY_PLAYLIST_ID,
            items=map(lambda track: track.uri, tracks),
        )

        spotify.change_playlist_details(
            HISTORY_PLAYLIST_ID,
            description=f"Last 50 songs played. Updated at {timestamp()}",
        )

        return JsonResponse(data={"tracks": list(map(str, tracks))})
