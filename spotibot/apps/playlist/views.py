import logging

from django.http.response import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from rest_framework.status import HTTP_400_BAD_REQUEST

from spotibot.apps.track.models import Track
from spotibot.auth import ValidateApiKey
from spotibot.spotify import api
from .serializers import UpdatePlaylistSerializer

logger = logging.getLogger(__name__)


class PlaylistUpdateView(GenericAPIView):
    permission_classes = [ValidateApiKey]
    serializer_class = UpdatePlaylistSerializer

    def work(self, request, playlist_id: str, clear: bool):
        data: dict = JSONParser().parse(request)
        serialized: Serializer = self.get_serializer(data=data)

        if not serialized.is_valid():
            logger.warning("Bad request", extra={"request": request})
            return JsonResponse(
                status=HTTP_400_BAD_REQUEST, data={"errors": serialized.errors}
            )

        tracks, uris = [], []

        title = serialized["title"].value
        description = serialized["description"].value
        api.change_playlist_details(playlist_id, title, description)

        ids = serialized["ids"].value

        for track in map(Track.parse, api.client.tracks(ids)["tracks"]):
            tracks.append(str(track))
            uris.append(track.uri)

        api.update_playlist(playlist_id, uris, clear=clear)

        return JsonResponse(data={"playlist_id": playlist_id, "tracks": tracks})

    def patch(self, request, playlist_id: str):
        return self.work(request, playlist_id, False)

    def put(self, request, playlist_id: str):
        return self.work(request, playlist_id, True)
