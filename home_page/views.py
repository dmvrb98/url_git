from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UrlForm, ManageForm
from .models import UsersUrl
from random import randint
import random, string
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from bs4 import BeautifulSoup
import requests
from django.utils import timezone
from rest_framework import viewsets
from .serializers import UrlSerializer


def index(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["short"] == "":
                short = "".join(random.choice(string.ascii_letters) for x in range(10))
                input_url = UsersUrl(url=form.cleaned_data["url"], short=short)
                input_url.date_added = timezone.now()
                input_url.save()
                return redirect("home_page:index")

            else:
                input_url.date_added = timezone.now()
                input_url = form.save()
                return redirect("home_page:index")
    else:
        form = UrlForm()

    urls = UsersUrl.objects.all()
    context = {"form": form, "urls": urls}
    return render(request, "home_page/index.html", context)


def delete_url(request, UsersUrl_id):
    urls = get_object_or_404(UsersUrl, id=UsersUrl_id)
    if request.method == "GET":
        urls.delete()
        return redirect("home_page:index")
    return render(request, "home_page/index.html", context)


def redirect_url(request, short):
    fullurl = get_object_or_404(UsersUrl, short=short)
    fullurl.click_count += 1
    fullurl.save()

    page = requests.get(fullurl.url)
    soup = BeautifulSoup(page.text, "html.parser")

    content = soup.find("title")
    fullurl.url_content += content.text
    fullurl.save()
    return HttpResponseRedirect(fullurl.url)


def manage_url(request, UsersUrl_id):
    if request.method != "POST":
        form = ManageForm(request.POST)
        urls = UsersUrl.objects.get(id=UsersUrl_id)
    context = {"form": form, "urls": urls}
    return render(request, "home_page/manage_url.html", context)


class UrlViewSet(viewsets.ModelViewSet):
    queryset = UsersUrl.objects.all().order_by("id")
    serializer_class = UrlSerializer
