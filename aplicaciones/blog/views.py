from django.shortcuts import render
from aplicaciones.blog.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    posts = Post.objects.filter(estado=True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'detalle_post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='General')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='General'),
        ).distinct()

    return render(request, 'generales.html', {'posts': posts})


def programacion(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Programación'))
    return render(request, 'programacion.html', {'posts': posts})


def informacion_didactica(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Información Didáctica'))
    return render(request, 'informacion_didactica.html', {'posts': posts})


def info_carrera(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Información acerca de la carrera'))
    return render(request, 'info_carrera.html', {'posts': posts})


def actividades_formacion(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Actividades de Formación Vocacional'))
    return render(request, 'actividades_formacion.html', {'posts': posts})
