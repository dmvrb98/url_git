from django.urls import path, include
from . import views

app_name = 'home_page'

urlpatterns = [
    path('', views.index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path('', views.url_table, name="url_table"),
]
