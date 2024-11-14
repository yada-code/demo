from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from .models import License
from django.views.decorators.csrf import csrf_exempt
import json
def home(request):
    return HttpResponse("Welcome to the homepage!")