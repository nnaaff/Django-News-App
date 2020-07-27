from django.contrib import admin
from django.urls import path
from . import views

app_name = 'newsweb'

urlpatterns = [
    path('', views.homepage, name="home"),
]


