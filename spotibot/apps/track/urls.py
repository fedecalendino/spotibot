from django.urls import path

from .views import TrackCollectionView, TrackEntityView

urlpatterns = [
    path(
        route="",
        view=TrackCollectionView.as_view(),
        name="track_collection_view",
    ),
    path(
        route="<str:pk>",
        view=TrackEntityView.as_view(),
        name="track_entity_view",
    ),
]
