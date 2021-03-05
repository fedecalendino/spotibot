import json
import logging

from django.http.response import JsonResponse
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
