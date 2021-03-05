import pytz

from django.conf import settings
from django.utils import timezone

TIMEZONE = pytz.timezone(settings.TIMESTAMPS_TIMEZONE)


def timestamp():
    return timezone.now().astimezone(TIMEZONE).strftime("%b %d, %H:%M")
