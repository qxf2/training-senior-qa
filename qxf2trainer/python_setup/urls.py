#URLs configuration file for python setup
from django.urls import path
from . import views

urlpatterns = [
    path('before-you-begin', views.beforeyoubegin, name='beforeyoubegin'),
    path('what-to-expect', views.whattoexpect, name='whattoexpect'),
]
