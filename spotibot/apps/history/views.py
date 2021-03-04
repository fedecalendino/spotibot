import logging
import json
from uuid import uuid4

from django.http.response import JsonResponse
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from spotibot.apps.models import Album, Artist, Track

from .models import History
from .serializers import HistorySerializer

logger = logging.getLogger(__name__)


class HistoryCollectionView(ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = []


class HistoryEntityView(RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = []


class HistoryParseView(CreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data = json.loads(request.read())

        artist = None
        features = []

        for index, data_artist in enumerate(data["track"]["artists"]):
            obj, _ = Artist.objects.all().get_or_create(
                id=data_artist["id"],
                name=data_artist["name"],
                uri=data_artist["uri"],
            )

            if index == 0:
                artist = obj
            else:
                features.append(obj)

        data_album = data["track"]["album"]

        album_artist, _ = Artist.objects.all().get_or_create(
            id=data_album["artists"][0]["id"],
            name=data_album["artists"][0]["name"],
            uri=data_album["artists"][0]["uri"],
        )

        album, _ = Album.objects.all().get_or_create(
            id=data_album["id"],
            name=data_album["name"],
            uri=data_album["uri"],
            artist=album_artist,
        )

        data_track = data["track"]

        track, _ = Track.objects.all().get_or_create(
            id=data_track["id"],
            name=data_track["name"],
            uri=data_track["uri"],
            artist=artist,
            album=album,
        )
        
        for feature in features:
            track.features.add(feature)

        track.save()

        history = History(id=str(uuid4()), track=track, played_at=data["played_at"], raw=data)
        history.save()

        return JsonResponse(data=HistorySerializer(history).data)
