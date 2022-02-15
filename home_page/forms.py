from django import forms
from .models import UsersUrl


class UrlForm(forms.ModelForm):
    class Meta:
        model = UsersUrl
        fields = [
            "url",
            "short",
        ]
        labels = {
            "url": "",
            "short": "",
        }
        widgets = {
            "url": forms.TextInput(
                attrs={
                    "size": "50",
                    "placeholder": "Your URL",
                }
            ),
            "short": forms.TextInput(
                attrs={
                    "size": "35",
                    "placeholder": "Your short URL(optional)",
                },
            ),
        }


class ManageForm(forms.ModelForm):
    class Meta:
        model = UsersUrl
        fields = ["short", "url_content", "click_count", "date_added"]
        labels = {"short": "", "url_content": "", "click_count": "", "date_added": ""}
        widgets = {}
