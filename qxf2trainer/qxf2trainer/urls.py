"""qxf2trainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('tutorials/', include('tutorials.urls')),
    path('python-setup/', include('python_setup.urls')),
    path('vscode-setup/', include('vscode_setup.urls')),
    path('chrome-driver-setup/', include('chrome_driver_setup.urls')),
    path('git-bash-setup/', include('git_bash_setup.urls')),
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
