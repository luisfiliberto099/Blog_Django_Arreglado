from django.shortcuts import render
from aplicaciones.blog.models import *
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.filter(estado=True)
    print(posts)
    return render(request, 'index.html', {'posts': posts})

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'detalle_post':post})

def generales(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='General'))
    return render(request, 'generales.html', {'posts': posts})


def programacion(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Programación'))
    return render(request, 'programacion.html', {'posts': posts})


def tutoriales(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Tutoriales'))
    return render(request, 'tutoriales.html', {'posts': posts})


def tecnologia(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Tecnologia'))
    return render(request, 'tecnologia.html', {'posts': posts})


def videojuegos(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Videojuegos'))
    return render(request, 'videojuegos.html', {'posts': posts})
