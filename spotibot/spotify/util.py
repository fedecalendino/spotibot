import pytz

from django.conf import settings
from django.utils import timezone

TIMEZONE = pytz.timezone(settings.TIMESTAMPS_TIMEZONE)


def chunks(list_: list, size: int):
    for i in range(0, len(list_), size):
        yield list_[i : i + size]


def timestamp():
    return timezone.now().astimezone(TIMEZONE).strftime("%b %d, %H:%M")
