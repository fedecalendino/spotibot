import logging

from django.http.response import JsonResponse
from rest_framework.generics import GenericAPIView

from spotibot.auth import ValidateApiKey
from spotibot.spotify import jobs

logger = logging.getLogger(__name__)


class DiscoverJobView(GenericAPIView):
    permission_classes = [ValidateApiKey]

    def get(self, _):
        items = jobs.discover.run()
        return JsonResponse(data={"items": list(map(str, items))})


class HistoryJobView(GenericAPIView):
    permission_classes = [ValidateApiKey]

    def get(self, _):
        items = jobs.history.run()
        return JsonResponse(data={"items": list(map(str, items))})


class WeekliesJobView(GenericAPIView):
    permission_classes = [ValidateApiKey]

    def get(self, _):
        items = jobs.weeklies.run()
        return JsonResponse(data={"items": list(map(str, items))})


class UpdateJobView(GenericAPIView):
    permission_classes = [ValidateApiKey]

    def get(self, _):
        jobs.update.run()
        return JsonResponse(data={})
