from django.test import TestCase
from django.urls import reverse

from url_shortener.models import URL


class URLTestCase(TestCase):
    def setUp(self):
        self.url = URL.objects.create(original="http://example.com")

    def test_short_url_is_generated(self):
        self.assertIsNotNone(self.url.shortened)
        self.assertGreater(len(self.url.shortened), 0)

    def test_redirects(self):
        request = self.client.get(reverse("redirect", kwargs={"short_url": self.url.shortened}), follow=True)

        self.assertRedirects(request, "http://example.com")
