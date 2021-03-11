import logging
from typing import List

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import BaseFilterBackend, OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from spotibot.auth import ValidateApiKey

from .models import Track
from .serializers import TrackSerializer

logger = logging.getLogger(__name__)


class TrackCollectionView(ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [ValidateApiKey]

    ordering_fields = ["name"]
    search_fields = ["name"]
    filterset_fields = {
        "name": ["exact"],
        "duration": ["exact"],
        "artist__name": ["exact"],
        "album__name": ["exact"],
    }

    @property
    def filter_backends(self) -> List[BaseFilterBackend]:
        return [DjangoFilterBackend, SearchFilter, OrderingFilter]


class TrackEntityView(RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [ValidateApiKey]
