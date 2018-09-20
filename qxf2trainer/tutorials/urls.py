#URLs configuration file for tutorials
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tutorialshome'),
    path('welcome', views.welcome, name='welcome'),
    path('what-to-expect', views.what_to_expect, name='what-to-expect'),
]
