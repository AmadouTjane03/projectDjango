from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')


def index(request):
    return HttpResponse("Bienvenue sur la page d'accueil de notre site.")

def about(request):
    return HttpResponse("À propos de notre site.")




