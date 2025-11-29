from django.apps import apps as django_apps


def register_applications(**_kwargs):
    Application = django_apps.get_model("meta", "Application")

    for app_config in django_apps.get_app_configs():
        Application.objects.update_or_create(
            name=app_config.name,
            defaults={
                "label": app_config.label,
                "verbose_name": app_config.verbose_name,
            },
        )
