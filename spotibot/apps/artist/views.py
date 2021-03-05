import logging

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from spotibot.auth import ValidateApiKey
from .models import Artist
from .serializers import ArtistSerializer

logger = logging.getLogger(__name__)


class ArtistCollectionView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [ValidateApiKey]


class ArtistEntityView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [ValidateApiKey]
