from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('registration', registration, name='registration'),
    path('hospitalization', hospitalization, name='hospitalization'),
    path('diagnostic', diagnostic, name='diagnostic'),
]