from django.shortcuts import render
from django.http import HttpResponse

from .models import squirrel

def all_squirrels(request):
    squirrels = squirrel.objects.all()
    context = {
        'squirrels': pets,
    }
    return render(request, 'sightings/all.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
