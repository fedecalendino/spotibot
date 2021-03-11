import logging

from django.http.response import JsonResponse
from rest_framework.generics import GenericAPIView

logger = logging.getLogger(__name__)


class HeartbeatView(GenericAPIView):
    swagger_schema = None

    def get(self, _):
        return JsonResponse(data={"korok": "yahaha! you found me! 🌿️"})
