import logging
from typing import List

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import BaseFilterBackend, OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from spotibot.auth import ValidateApiKey
from .models import Artist
from .serializers import ArtistSerializer

logger = logging.getLogger(__name__)


class ArtistCollectionView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [ValidateApiKey]

    ordering_fields = ["name"]
    search_fields = ["name"]
    filterset_fields = {
        "name": ["exact"],
    }

    @property
    def filter_backends(self) -> List[BaseFilterBackend]:
        return [DjangoFilterBackend, SearchFilter, OrderingFilter]


class ArtistEntityView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [ValidateApiKey]
