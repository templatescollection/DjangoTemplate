"""Basic tests for the Django project."""

from django.test import TestCase
from django.urls import reverse


class BasicTestCase(TestCase):
    """Basic test cases for the Django application."""

    def test_admin_url_exists(self) -> None:
        """Test that admin URL is accessible."""
        url = reverse("admin:index")
        response = self.client.get(url)
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)

    def test_health_check(self) -> None:
        """Test basic health check."""
        # This is a placeholder - add actual health check endpoint test
        self.assertTrue(True)
