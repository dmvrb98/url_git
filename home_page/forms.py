from django import forms
from .models import UsersUrl


class UrlForm(forms.ModelForm):
	class Meta:
		model = UsersUrl
		fields = ('url', 'short',)
		labels = {'url': '',
				  'short': '',}
		widgets = {
			'url': forms.TextInput(attrs={
			'class': 'col-6', 
			'placeholder': 'Your URL', }),

				  'short': forms.TextInput(attrs={
				  	'class': 'col',
				  	'placeholder': 'Your short URL(optional)',}),
					}