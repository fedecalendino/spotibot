from django.urls import path

from . import views

urlpatterns = [
    path(
        route="<str:playlist_id>",
        view=views.PlaylistUpdateView.as_view(),
        name="playlist_update_view",
    ),
]
