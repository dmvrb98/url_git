from .models import UsersUrl
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersUrl
        fields = ("url", "short", "url_content", "date_added", "click_count")
