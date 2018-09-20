#URLs configuration file for tutorials
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tutorialshome'),
]
