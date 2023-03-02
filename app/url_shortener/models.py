from django.db import models

from url_shortener.utils import generate_short_url


class URL(models.Model):
    original = models.URLField(unique=True)
    shortened = models.CharField(max_length=20, unique=True, default=generate_short_url)
