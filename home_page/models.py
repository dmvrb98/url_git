from django.db import models
from django.contrib.auth.models import User


class UsersUrl(models.Model):
    url = models.CharField(max_length=200)
    short = models.CharField(
        max_length=10, blank=True, unique=True, error_messages={"unique": ""}
    )
    date_added = models.DateTimeField(null=True)
    click_count = models.IntegerField(default=0)
    url_content = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.url[:150]}..."
