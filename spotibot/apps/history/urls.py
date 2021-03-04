from django.urls import path

from .views import HistoryCollectionView, HistoryEntityView, HistoryParseView

urlpatterns = [
    path(
        route="",
        view=HistoryCollectionView.as_view(),
        name="history_collection_view",
    ),
    path(
        route="parse",
        view=HistoryParseView.as_view(),
        name="history_parse_view",
    ),
    path(
        route="<str:pk>",
        view=HistoryEntityView.as_view(),
        name="history_entity_view",
    ),
]
