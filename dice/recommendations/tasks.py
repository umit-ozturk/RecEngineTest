from config import celery_app
from dice.recommendations.models import Recommendation


@celery_app.task()
def get_recommendations_count():
    """A pointless Celery task to demonstrate usage."""
    return Recommendation.objects.count()
