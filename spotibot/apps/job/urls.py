from django.urls import path

from . import views

urlpatterns = [
    path(
        route="discover",
        view=views.DiscoverJobView.as_view(),
        name="discover_job_view",
    ),
    path(
        route="history",
        view=views.HistoryJobView.as_view(),
        name="history_job_view",
    ),
    path(
        route="weeklies",
        view=views.WeekliesJobView.as_view(),
        name="weeklies_job_view",
    ),
    path(
        route="update",
        view=views.UpdateJobView.as_view(),
        name="update_job_view",
    ),
]
