from django.urls import path

from .views import HistoryCollectionView, HistoryEntityView

urlpatterns = [
    path(
        route="",
        view=HistoryCollectionView.as_view(),
        name="history_collection_view",
    ),
    path(
        route="<str:pk>",
        view=HistoryEntityView.as_view(),
        name="history_entity_view",
    ),
]
