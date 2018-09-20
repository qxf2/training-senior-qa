from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Welcome to the Qxf2 trainer!</h2><p>You are just a login away from learning some cool new tech!<br><a href=\"accounts/login\">Log in</a></p>")