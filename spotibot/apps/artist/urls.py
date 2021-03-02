from django.urls import path

from .views import ArtistCollectionView, ArtistEntityView

urlpatterns = [
    path(
        route="",
        view=ArtistCollectionView.as_view(),
        name="artist_collection_view",
    ),
    path(
        route="<str:artist_id>",
        view=ArtistEntityView.as_view(),
        name="artist_entity_view",
    ),
]
