from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def beforeyoubegin(request):
    return HttpResponse("<h2>Before you begin</h2> <p>We would like to remind you of a few things. <ol><li>It is OK to run into issues during this step. Setup issues are a part of regular work.</li><li>It is OK to not know what you are doing. Things will come together later in the course.</li></ol></p><br><h2>Take a moment</h2><p>Until you have the momentum of several small technical accomplishments, take a moment to figure out how you are feeling. This exercise will help you combat some unrealistic defense mechanisms at a later date!</p><a href=\"what-to-expect\">Next</a>")

@login_required
def whattoexpect(request):
    return HttpResponse("<h2>What to expect</h2>\
    <p>At the end of this mini-tutorial, you can expect to have setup Python on your machine.</p> \
    <p>Most tutorials and training material expect things to go smoothly. Not us! We are experienced professional QA and we know that a lot can go wrong during setup. It's probably not your fault. So before we begin, here is what to expect as you go through the tutorial. \
    <ol>\
    <li>Beginners usually have trouble with setup. That's ok.</li>\
    <li>Over time, you will develop a mental catalogue of problems that come with install and setup.</li>\
    </ol>\
    </p>\
    <h3>If/When you hit an issue</h3>When you run into an issue, don't panic. Here is what you can try<ol><li>Take a minute to try and read through the error message. It's ok if seems like gibberish ... just make the attempt.</li><li>Try and identify the key line in the error</li><li>Google for the phrase 'python install <your OS name e.g.: windows> <key line in error>'</li><li>Try out the suggestions mentioned in the Google search results even if you don't fully understand them.</li><li>After you have tried your best, contact Qxf2 on our public Slack Channel</li></ol></p><br><a href=\"tutorial\">Next</a>")

@login_required
def install_python(request):
    return HttpResponse("<p>We expect this exercise to take you somewhere between 15-minutes to 2 hours. If you take more than two hours, please post what you tried along wtih error messages to our slack channel.</p><p>Python has two versions (3.x and 2.7.x) and multiple distributions (IronPython, Conda, etc.). Python 3.x is the latest and ideally what we would all use. We'd love to recommend you use Python 3.x. However, for this tutorial, you are going to install the latest Python 2.7 version from the official site. We are doing this because we find many QA departments have not yet embraced Python 3.x  and we want these tutorials to be as close to your real work as possible. In keeping with our approach of helping you think in different ways, we have three approaches that work. There is no shame or pride in choosing anyone of them. Just choose the method you are comfortable with and proceed.</p><br>\
    <h3>Approach 1: Try it out yourself</h3><ol><li>We'd like to promote independent thinking and problem solving. So if you feel ready, try to install Python without referring to any documentation</li></ol><br>\
    <h3>Approach 2: Google for instructions</h3><ol><li>Google for Python 2.7 install <your operating system name></li><li>Follow the instructions</li></ol><br>\
    <h3>Approach 3: follow this guide</h3><ol><li>Visit <a href=\"https://www.python.org/downloads/\">https://www.python.org/downloads/</a></li><li>Ignore the 3.x versions and click on the latest 2.7.x release</li><li>On the release page, choose Python 2.7 release for your operating system </li><li>Download the executable and follow the steps</li></ol><br>\
    <h3>Exercise</h3><p>Once you are done, add the Python executable to your path environment variable. Hint: Google for 'add Python to path environment variable <your os name>'.</p><h3>Verify your setup</h3><p>After you are done with the exercise listed above, it is time to verify your Python installation. It is a good habit to take small steps and verify them immediately. This will help you avoid getting stuck later on. To verify your setup, pull up your terminal prompt and type python --version. You should see the version you installed listed.</p><br><a href=\"did-you-complete\">Next</a>")

@login_required
def didyoucomplete(request):
    return HttpResponse("<h3>Did you finish?</h3><input type=\"checkbox\" name=\"easy\" value=\"Easy\"> Yes, quite easily <br><input type=\"checkbox\" name=\"medium\" value=\"medium\"> Yes, but with some difficulty <br><input type=\"checkbox\" name=\"hard\" value=\"hard\"> No, I am stuck <br><br><h2>Take a moment</h2><p>Until you have the momentum of several small technical accomplishments, take a moment to figure out how you are feeling. How does it compare to how you felt before starting the task?</p><br><br><a href=\"once-you-complete\">Next</a>")

@login_required
def onceyoucomplete(request):
    return HttpResponse("<p>Now that you are done with this setup exercise, here is a habit we would like you to pick - start using Stack Overflow when you have a problem that you cannot solve.</p><h3>Stack Overflow</h3> <strong>Fact:</strong>All developers run into problems with their code every single day. But they have a very nice resource called <a href=\"https://stackoverflow.com\">Stack Overflow</a>. Stack Overflow is a question answer site for developers. Almost any issue you hit through this series of tutorials would have already been asked and solved on Stack Overflow. From now on, when you Google for a technical question, lookout for Stack Overflow links and learn to try out the first or second accepted answer.</p><br><a href=\"../tutorials\">Back to tutorial list</a>")