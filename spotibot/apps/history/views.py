import logging
import json
from uuid import uuid4

from django.http.response import JsonResponse
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

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
        history = History.parse(data)

        return JsonResponse(data=HistorySerializer(history).data)
