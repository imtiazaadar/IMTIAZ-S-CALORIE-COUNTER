# Imtiaz Adar
# Calorie Counter App
# Python
# Django
# Phone : +8801778767775
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foodcalorieapp.urls'))
]
