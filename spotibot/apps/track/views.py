import logging

from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Track
from .serializers import TrackSerializer

logger = logging.getLogger(__name__)


class TrackCollectionView(ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [GenericAPIView]


class TrackEntityView(RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [GenericAPIView]
