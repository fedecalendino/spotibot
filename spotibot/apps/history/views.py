import json
import logging
from typing import List

from django.http.response import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import BaseFilterBackend, OrderingFilter, SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from spotibot.auth import ValidateApiKey
from .models import History
from .serializers import HistorySerializer

logger = logging.getLogger(__name__)


class HistoryCollectionView(ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [ValidateApiKey]

    ordering_fields = ["played_at"]
    search_fields = ["track__name"]
    filterset_fields = {
        "track__name": ["exact"],
        "track__artist__name": ["exact"],
        "track__album__name": ["exact"],
    }

    @property
    def filter_backends(self) -> List[BaseFilterBackend]:
        return [DjangoFilterBackend, SearchFilter, OrderingFilter]


class HistoryEntityView(RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [ValidateApiKey]


class HistoryParseView(CreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [ValidateApiKey]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.read())
        history = History.parse(data)

        return JsonResponse(data=HistorySerializer(history).data)
