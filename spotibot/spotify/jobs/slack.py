from slack_webhook import Slack
from django.conf import settings


SLACK = Slack(url=settings.SLACK_WEBHOOK_URL)


def notify(job):
    def wrapper(*args, **kwargs):
        result = job(*args, **kwargs)
        SLACK.post(text=f"spotibot.{job.__module__.split('.')[-1]} finished.")

        return result

    return wrapper
