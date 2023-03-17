from django.shortcuts import render
from django.http import HttpResponse
import random
# import string

# Create your views here.


def home(request):
    return render(request, 'web01/home.html', {'name': 'Ethi'})
