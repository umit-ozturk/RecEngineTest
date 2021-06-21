from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RecommendationsConfig(AppConfig):
    name = "dice.recommendations"
    verbose_name = _("Recommendations")

    def ready(self):
        try:
            import dice.recommendations.signals  # noqa F401
        except ImportError:
            pass
