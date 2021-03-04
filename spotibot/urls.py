from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/albums/", include("spotibot.apps.album.urls")),
    path("api/artists/", include("spotibot.apps.artist.urls")),
    path("api/tracks/", include("spotibot.apps.track.urls")),
]
