from django.urls import path
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', home),
]