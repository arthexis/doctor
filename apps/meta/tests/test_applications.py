from django.apps import apps
from django.test import TestCase

from apps.meta.models import Application


class ApplicationRegistrationTests(TestCase):
    def test_applications_populated_from_registry(self):
        registered = {app_config.name: app_config for app_config in apps.get_app_configs()}
        applications = Application.objects.all()

        self.assertEqual(applications.count(), len(registered))

        for application in applications:
            app_config = registered[application.name]
            self.assertEqual(application.label, app_config.label)
            self.assertEqual(application.verbose_name, app_config.verbose_name)
