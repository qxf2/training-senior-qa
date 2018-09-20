#URLs configuration file for tutorials
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('welcome', views.welcome, name='Welcome'),
    path('what-to-expect', views.what_to_expect, name='What to expect'),
]
