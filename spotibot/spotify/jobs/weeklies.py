import logging
from typing import List

from django.conf import settings
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import ExtractYear, ExtractWeek

from spotibot.apps.history.models import History
from spotibot.spotify import api
from spotibot.spotify import util

logger = logging.getLogger(__name__)


WEEKLIES_PLAYLIST_ID = settings.SPOTIFY["PLAYLISTS"]["WEEKLIES"]
TOP = 3


def run() -> List[str]:
    items = []

    current_year, current_week, _ = timezone.now().isocalendar()

    for week in range(1, current_week + 1):
        queryset = (
            History.objects.annotate(year=ExtractYear("played_at"))
            .filter(year=current_year)
            .annotate(week=ExtractWeek("played_at"))
            .filter(week=week)
            .values("track__name", "track__uri", "week")
            .annotate(total=Count("played_at"))
            .order_by("-total")
        )

        items.extend(queryset.all()[:TOP])

    api.update_playlist(
        WEEKLIES_PLAYLIST_ID[str(current_year)],
        items=map(lambda item: item["track__uri"], items),
    )

    api.change_playlist_details(
        WEEKLIES_PLAYLIST_ID[str(current_year)],
        description=f"Top {TOP} for each week of {current_year}. "
        f"Current week: {current_week}. "
        f"Updated at {util.timestamp()}",
    )

    return list(
        map(
            lambda item: f'{item["track__name"]} | {item["week"]} | {item["total"]}',
            items,
        )
    )
