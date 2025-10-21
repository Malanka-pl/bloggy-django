from django.http import HttpResponse
from django.shortcuts import render
from .models import Greeting


def index(request):
    return HttpResponse('Hi, I’m Cat — Django learner')


def contact_view(request):
    return render(request, 'contact.html')


def greeting_view(request):
    all_greetings = Greeting.objects.all
    return render(request, 'greeting.html', context={'data': all_greetings})

