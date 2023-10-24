from django.contrib import admin
from django.urls import path, include
from accountio import views

urlpatterns = [
    path('/login', views.PrivateUserLogin.as_view(), name='user_login'),
    path('/register', views.PublicUserRegistration.as_view(), name='user_registration'),
]
