from config import celery_app
from dice.artists.models import Artist


@celery_app.task()
def get_artists_count():
    """A pointless Celery task to demonstrate usage."""
    return Artist.objects.count()
