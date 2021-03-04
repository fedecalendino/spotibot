from django.urls import path

from .views import TrackCollectionView, TrackEntityView

urlpatterns = [
    path(
        route="",
        view=TrackCollectionView.as_view(),
        name="track_collection_view",
    ),
    path(
        route="<str:track_id>",
        view=TrackEntityView.as_view(),
        name="track_entity_view",
    ),
]
