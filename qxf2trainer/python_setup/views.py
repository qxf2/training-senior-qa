from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader

# Create your views here.
@login_required
def beforeyoubegin(request):
    template = loader.get_template('python_setup/before-you-begin.html')
    return HttpResponse(template.render())

@login_required
def whattoexpect(request):
    template = loader.get_template('python_setup/what-to-expect.html')
    return HttpResponse(template.render())

@login_required
def install_python(request):
    template = loader.get_template('python_setup/tutorial.html')
    return HttpResponse(template.render())

@login_required
def didyoucomplete(request):
    return HttpResponse("<h3>Did you finish?</h3><input type=\"checkbox\" name=\"easy\" value=\"Easy\"> Yes, quite easily <br><input type=\"checkbox\" name=\"medium\" value=\"medium\"> Yes, but with some difficulty <br><input type=\"checkbox\" name=\"hard\" value=\"hard\"> No, I am stuck <br><br><h2>Take a moment</h2><p>Until you have the momentum of several small technical accomplishments, take a moment to figure out how you are feeling. How does it compare to how you felt before starting the task?</p><br><br><a href=\"once-you-complete\">Next</a>")

@login_required
def onceyoucomplete(request):
    return HttpResponse("<p>Now that you are done with this setup exercise, here is a habit we would like you to pick - start using Stack Overflow when you have a problem that you cannot solve.</p><h3>Stack Overflow</h3> <strong>Fact:</strong>All developers run into problems with their code every single day. But they have a very nice resource called <a href=\"https://stackoverflow.com\">Stack Overflow</a>. Stack Overflow is a question answer site for developers. Almost any issue you hit through this series of tutorials would have already been asked and solved on Stack Overflow. From now on, when you Google for a technical question, lookout for Stack Overflow links and learn to try out the first or second accepted answer.</p><br><a href=\"../tutorials\">Back to tutorial list</a>")