from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'med/index.html')

def registration(request):
    return render(request, 'med/registration.html')

def hospitalization(request):
    return render(request, 'med/hospitalization.html')

def diagnostic(request):
    return render(request, 'med/diagnostic.html')

#def registration(request):
#    if(request.GET):
#        print(request.GET)
#    return HttpResponse("<h1>Что-то</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')