from django.urls import path, include, re_path
from . import views
from rest_framework import routers

app_name = "home_page"

router = routers.DefaultRouter()
router.register(r"url", views.UrlViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path("", include("django.contrib.auth.urls")),
    path("manage_url/<int:UsersUrl_id>/", views.manage_url, name="manage_url"),
    path("<int:UsersUrl_id>/", views.delete_url, name="delete_url"),
    path("<short>/", views.redirect_url, name="redirect_url"),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
