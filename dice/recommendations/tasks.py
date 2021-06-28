from django.contrib.auth import get_user_model

from config import celery_app
from dice.recommendations.models import Recommendation
from rec_engine.recomendation import (
    get_recommendation_closest_artist,
    get_recommendation_closest_per_cluster,
)

User = get_user_model()


@celery_app.task()
def recommend_closest_artist(rec_id, k, user_embedding):
    """

    :param rec_id:
    :param k:
    :param user_embedding:
    :return:
    """
    recommendations = get_recommendation_closest_artist(k, user_embedding)
    rec_obj = Recommendation.objects.get(id=rec_id)
    rec_obj.recommends = recommendations
    rec_obj.save()


@celery_app.task()
def recommend_closest_per_cluster(rec_id, k, user_embedding):
    """

    :param rec_id:
    :param k:
    :param user_embedding:
    :return:
    """
    recommendations = get_recommendation_closest_per_cluster(k, user_embedding)
    rec_obj = Recommendation.objects.get(id=rec_id)
    rec_obj.recommends = recommendations
    rec_obj.save()


@celery_app.task()
def get_recommendations_count():
    """A pointless Celery task to demonstrate usage."""
    return Recommendation.objects.count()
