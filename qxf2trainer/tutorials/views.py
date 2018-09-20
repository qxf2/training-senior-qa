from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the first page.")

def welcome(request):
    return HttpResponse("This is the welcome screen<br><a href=\"what-to-expect\">What to expect</a>")

def what_to_expect(request):
    return HttpResponse("This is the what to expect screen<br><a href=\"welcome\">Welcome</a>")