from django.urls import path, include, re_path
from . import views

app_name = 'home_page'

urlpatterns = [
    path('', views.index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path('manage_url/<int:UsersUrl_id>/', views.manage_url, name="manage_url"),
    path('<int:UsersUrl_id>/', views.delete_url, name="delete_url"),
    path('<short>/', views.redirect_url, name="redirect_url"),
]
