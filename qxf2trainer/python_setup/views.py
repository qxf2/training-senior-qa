from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def beforeyoubegin(request):
    return HttpResponse("<h2>Before you begin</h2> <p>Before you begin, we would like to remind you of a few things. <ol><li>It is OK to run into issues during this step. Setup issues are a part of regular work.</li><li>It is OK to not know what you are doing. Things will come together later in the course.</li></ol></p><br><h3>Take a moment ...</h3><p>Until you have the momentum of several small technical accomplishments, take a moment to figure out how you are feeling. This exercise will help you combat some unrealistic defense mechanisms at a later date! Example of some feelings are: <ol><li>I am neutral</li><li>I'm excited that I am starting something new</li><li>I already know this. So this is a waste of my time</li><li>I don't even know what to feel right now</li></ol></p><a href=\"what-to-expect\">Next</a>")

def whattoexpect(request):
    return HttpResponse("<h2>What to expect</h2> <p>Here is what to expect as you go through the tutorial. <ol><li>Beginners always have trouble with setup. That's ok.</li><li>Over time, you will develop a mental catalogue of problems that come with install and setup.</li></ol></p><br>")