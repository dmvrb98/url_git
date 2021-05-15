from django.db import models
from django.contrib.auth.models import User


class UsersUrl(models.Model):
	url = models.CharField(max_length=100)
	short = models.CharField(max_length=10)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.url


