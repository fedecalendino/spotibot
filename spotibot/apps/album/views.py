import logging

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from spotibot.auth import ValidateApiKey
from .models import Album
from .serializers import AlbumSerializer

logger = logging.getLogger(__name__)


class AlbumCollectionView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [ValidateApiKey]


class AlbumEntityView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [ValidateApiKey]
