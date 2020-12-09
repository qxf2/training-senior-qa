from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader

# Create your views here.


@login_required
def beforeyoubegin(request):
    template = loader.get_template('chrome_driver_setup/before-you-begin.html')
    return HttpResponse(template.render())


@login_required
def whattoexpect(request):
    template = loader.get_template('chrome_driver_setup/what-to-expect.html')
    return HttpResponse(template.render())


@login_required
def install_chrome_driver(request):
    template = loader.get_template('chrome_driver_setup/tutorial.html')
    return HttpResponse(template.render())


@login_required
def didyoucomplete(request):
    template = loader.get_template('chrome_driver_setup/did-you-complete.html')
    return HttpResponse(template.render())


@login_required
def onceyoucomplete(request):
    template = loader.get_template(
        'chrome_driver_setup/once-you-complete.html')
    return HttpResponse(template.render())
