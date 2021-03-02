import logging

from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

logger = logging.getLogger(__name__)


class ArtistCollectionView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []


class ArtistEntityView(RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []
