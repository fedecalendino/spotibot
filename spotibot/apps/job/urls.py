from django.urls import path

from .views import DiscoverJobView, HistoryJobView

urlpatterns = [
    path(
        route="discover",
        view=DiscoverJobView.as_view(),
        name="discover_job_view",
    ),
    path(
        route="history",
        view=HistoryJobView.as_view(),
        name="history_job_view",
    ),
]
