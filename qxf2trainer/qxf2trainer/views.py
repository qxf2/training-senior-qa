from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Dummy login page to be replaced when our login screen is ready.<br><a href=\"tutorials/\">Log in</a>")