from django.shortcuts import render
from aplicaciones.blog.models import *


def home(request):
    posts = Post.objects.filter(estado=True)
    print(posts)
    return render(request, 'index.html', {'posts': posts})

def generales(request):
    posts = Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre = 'General'))
    return render(request, 'generales.html', {'posts': posts})

def programacion(request):
    return render(request, 'programacion.html')

def tutoriales(request):
    return render(request, 'tutoriales.html')


def tecnologia(request):
    return render(request, 'tecnologia.html')

def videojuegos(request):
    return render(request, 'videojuegos.html')