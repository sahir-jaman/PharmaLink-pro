from django.contrib import admin
from django.urls import path, include

# Authentication app Urls:
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth", include("accountio.urls")),
]
