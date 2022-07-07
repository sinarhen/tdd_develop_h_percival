from django.test import TestCase
from django.urls import resolve
from .views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    """Test of home page"""

    def test_root_url_resolves_to_home_page_view(self):
        """Test: the root url is converted to a view home page"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
