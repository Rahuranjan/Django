from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="home"),
    path('logout', views.logout, name="home"),
]