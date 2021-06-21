from django.contrib import admin

from dice.artists.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):

    list_display = ["id", "name", "image_url"]
    search_fields = ["name", "image_url"]
