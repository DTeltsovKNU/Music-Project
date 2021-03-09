from django.shortcuts import render
from django.http import HttpResponse
from .models import Songs

# Create your views here.

def home(request):
    songs = Songs.objects.order_by('title')
    return render(request, 'home/home.html',{'songs' : songs} )
