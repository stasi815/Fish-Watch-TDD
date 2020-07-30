from unittest import TestCase, main as unittest_main, mock
import json
import requests
from app import app

BASE_URL = 'https://www.fishwatch.gov/api/species/'
SAMPLE_SPECIES = 'Shortfin Squid'

class FishWatchTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """To these before each test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during the tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the Fish Watch landing page."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        page_content = result.get_data(as_text=True)
        self.assertIn('Index', page_content)

    def test_form(self):
        """Test the search form page"""
        result = self.client.get('/search_form')
        self.assertEqual(result.status, '200 OK')
        page_content = result.get_data(as_text=True)
        self.assertIn('Form', page_content)

    def test_get_all(self):
        r = requests.get(BASE_URL)
        response = r.json()
        self.assertEqual(r.status_code, 200)
        result = self.client.get('/all_species')
        self.assertEqual(result.status, '200 OK')

    def test_get_one(self):
        r = requests.get(f'{BASE_URL}{SAMPLE_SPECIES}')
        self.assertEqual(r.status_code, 200)



if __name__ == '__main__':
    unittest_main()