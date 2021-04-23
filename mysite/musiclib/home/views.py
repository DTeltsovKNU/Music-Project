from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs, Albums
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf

# Create your views here.

def home(request):
    songs = Songs.objects.order_by('title')
    return render(request, 'home/home.html', {'songs' : songs} )


def signup(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(home)
    else:
        form = UserCreationForm()
    args['form'] = form
    return render(request, 'home/signup.html', args)