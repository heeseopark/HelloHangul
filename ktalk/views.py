from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ktalk/index.html')


def submit_conversation(request):
    return HttpResponseRedirect('/ktalk/index')