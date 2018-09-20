from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("tutorials")
    else:
        return HttpResponseRedirect("accounts/login")