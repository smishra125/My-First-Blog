from django.urls import path, include
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.PersonView.as_view()),
    path('addweather', views.WeatherView.as_view()),


]