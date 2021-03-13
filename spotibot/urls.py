from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("heartbeat", include("spotibot.apps.heartbeat.urls")),
    path("api/albums/", include("spotibot.apps.album.urls")),
    path("api/artists/", include("spotibot.apps.artist.urls")),
    path("api/history/", include("spotibot.apps.history.urls")),
    path("api/jobs/", include("spotibot.apps.job.urls")),
    path("api/playlists/", include("spotibot.apps.playlist.urls")),
    path("api/tracks/", include("spotibot.apps.track.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("admin/", admin.site.urls))
    urlpatterns.append(path("docs/", include("spotibot.apps.docs.urls")))
