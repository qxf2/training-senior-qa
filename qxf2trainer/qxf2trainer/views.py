from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the first page.<br><a href=\"tutorials/what-to-expect\">What to expect</a><br><a href=\"tutorials/welcome\">Welcome</a>")