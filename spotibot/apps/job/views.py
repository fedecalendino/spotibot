import logging

from rest_framework.generics import GenericAPIView
from django.http.response import JsonResponse

from spotibot.api import spotify

logger = logging.getLogger(__name__)


class DiscoverJobView(GenericAPIView):
    def get(self, request):
        return JsonResponse(data=spotify.get_saved_tracks(limit=50))


class HistoryJobView(GenericAPIView):
    def get(self, request):
        return JsonResponse(data=spotify.get_history())
