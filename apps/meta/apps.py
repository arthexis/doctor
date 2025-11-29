from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MetaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.meta"

    def ready(self):
        from .signals import register_applications

        post_migrate.connect(register_applications, sender=self)
