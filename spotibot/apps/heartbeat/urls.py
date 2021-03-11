from django.urls import path

from . import views

urlpatterns = [
    path(
        route="",
        view=views.HeartbeatView.as_view(),
        name="heartbeat_view",
    ),
]
