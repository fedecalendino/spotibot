from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include("spotibot.apps.docs.urls")),
    path("api/albums/", include("spotibot.apps.album.urls")),
    path("api/artists/", include("spotibot.apps.artist.urls")),
    path("api/history/", include("spotibot.apps.history.urls")),
    path("api/jobs/", include("spotibot.apps.job.urls")),
    path("api/tracks/", include("spotibot.apps.track.urls")),
]
