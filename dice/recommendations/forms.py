from django.forms import ModelForm

from dice.recommendations.models import Recommendation


class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ["count", "method"]
