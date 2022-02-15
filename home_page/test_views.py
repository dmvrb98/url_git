import pytest
from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    assert User.objects.count() == 1
