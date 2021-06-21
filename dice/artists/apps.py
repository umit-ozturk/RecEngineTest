from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArtistsConfig(AppConfig):
    name = "dice.artists"
    verbose_name = _("Artists")

    def ready(self):
        try:
            import dice.artists.signals  # noqa F401
        except ImportError:
            pass
