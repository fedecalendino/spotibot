import logging
from typing import List

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import BaseFilterBackend, OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from spotibot.auth import ValidateApiKey
from .models import Album
from .serializers import AlbumSerializer

logger = logging.getLogger(__name__)


class AlbumCollectionView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [ValidateApiKey]

    ordering_fields = ["name"]
    search_fields = ["name"]
    filterset_fields = {
        "name": ["exact"],
        "artist__name": ["exact"],
    }

    @property
    def filter_backends(self) -> List[BaseFilterBackend]:
        return [DjangoFilterBackend, SearchFilter, OrderingFilter]


class AlbumEntityView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [ValidateApiKey]
