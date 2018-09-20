from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the first page.<br><br><h3>SETUP</h3><p>In this section, you will be guided to setup your environment. Proceed in order. Click on the first link/task that you are yet to complete.</p><ol><li><a href=\"../python-setup/before-you-begin\">Setup Python</a></li></ol><br><br><h3>EXERCISES</h3><p>To be filled as we go through the hackathon</p>")