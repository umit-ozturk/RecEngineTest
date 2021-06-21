from django.contrib import admin

from dice.recommendations.models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "recommends",
    ]
    search_fields = [
        "user",
    ]
