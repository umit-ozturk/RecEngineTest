from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from dice.recommendations.forms import RecommendationForm
from dice.recommendations.models import Recommendation


class RecommendationCreateView(LoginRequiredMixin, CreateView):

    model = Recommendation
    form_class = RecommendationForm


class RecommendationListView(LoginRequiredMixin, ListView):

    model = Recommendation

    def get_queryset(self):
        return Recommendation.objects.filter(user=self.request.user.username)
