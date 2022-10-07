from django.contrib import admin
from aplicaciones.blog.models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion')

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellidos']
    list_display = ('nombre', 'apellidos', 'estado', 'fecha_creacion')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)