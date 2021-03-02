import logging

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Artist
from .serializers import ArtistSerializer

logger = logging.getLogger(__name__)


class ArtistCollectionView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []


class ArtistEntityView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []
