from django.shortcuts import render
from django.http import HttpResponse
from .models import rooms
# Create your views here.

def index(request):
    ros = rooms.objects.all()
    return render(request,"index.html", {'ros' : ros})
