from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from dice.recommendations.constants import CLOSEST_ARTIST, CLOSEST_CLUSTER
from dice.recommendations.forms import RecommendationForm
from dice.recommendations.models import Recommendation
from dice.recommendations.tasks import (
    recommend_closest_artist,
    recommend_closest_per_cluster,
)


class RecommendationCreateView(LoginRequiredMixin, CreateView):

    model = Recommendation
    form_class = RecommendationForm

    def form_valid(self, form):
        recommendation = form.save(commit=False)
        recommendation.user = self.request.user
        recommendation.save()

        if recommendation.method == CLOSEST_ARTIST:
            recommend_closest_artist.delay(
                recommendation.id,
                recommendation.count,
                self.request.user.embedding,
            )
        if recommendation.method == CLOSEST_CLUSTER:
            recommend_closest_per_cluster.delay(
                recommendation.id,
                recommendation.count,
                self.request.user.embedding,
            )
        return super(RecommendationCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("recommendations:list")


class RecommendationListView(LoginRequiredMixin, ListView):

    model = Recommendation

    def get_queryset(self):
        return Recommendation.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RecommendationListView, self).get_context_data()
        print(context)
        print("-----------")
        return context
