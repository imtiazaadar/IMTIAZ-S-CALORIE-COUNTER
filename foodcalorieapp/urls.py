from django.contrib import admin
from django.urls import path
from . import views
# Imtiaz Adar
# Calorie Counter App
# Python
# Django
# Phone : +8801778767775
urlpatterns = [
    path('',views.web_homepage, name='homepageweb'),
]
