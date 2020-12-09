
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader

# Create your views here.


@login_required
def beforeyoubegin(request):
    template = loader.get_template('git_bash_setup/before-you-begin.html')
    return HttpResponse(template.render())


@login_required
def whattoexpect(request):
    template = loader.get_template('git_bash_setup/what-to-expect.html')
    return HttpResponse(template.render())


@login_required
def install_gitbash(request):
    template = loader.get_template('git_bash_setup/tutorial.html')
    return HttpResponse(template.render())


@login_required
def didyoucomplete(request):
    template = loader.get_template('git_bash_setup/did-you-complete.html')
    return HttpResponse(template.render())


@login_required
def onceyoucomplete(request):
    template = loader.get_template('git_bash_setup/once-you-complete.html')
    return HttpResponse(template.render())
