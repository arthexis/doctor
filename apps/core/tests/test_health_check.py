from django.test import Client, TestCase


class HealthCheckTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health_check_returns_ok_status(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
