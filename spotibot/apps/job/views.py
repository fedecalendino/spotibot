import logging

from django.http.response import JsonResponse
from rest_framework.generics import GenericAPIView

from spotibot.spotify import jobs

logger = logging.getLogger(__name__)


class DiscoverJobView(GenericAPIView):
    def get(self, _):
        pass


class HistoryJobView(GenericAPIView):
    def get(self, _):
        items = jobs.history.run()
        return JsonResponse(data={"items": list(map(str, items))})
