from django.urls import path

from .views import AlbumCollectionView, AlbumEntityView

urlpatterns = [
    path(
        route="",
        view=AlbumCollectionView.as_view(),
        name="album_collection_view",
    ),
    path(
        route="<str:pk>",
        view=AlbumEntityView.as_view(),
        name="album_entity_view",
    ),
]
