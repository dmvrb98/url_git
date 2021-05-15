from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UrlForm
from .models import UsersUrl


def index(request):
	if request.method == 'POST':
		form = UrlForm(request.POST)
		if form.is_valid():
			input_url = form.save()
			input_url.owner = request.user
			return redirect('home_page:index')
	else:
		form = UrlForm()


	context = {'form': form}
	return render(request, 'home_page/index.html', context)

def url_table(request):
	urls = UsersUrl.objects.all()
	shorts = UsersUrl.objects.values('short')
	context = {'urls': urls, 'shorts': shorts}
	return render(request, 'home_page/index.html', context)