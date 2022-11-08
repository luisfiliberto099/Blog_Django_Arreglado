from django.contrib import admin
from aplicaciones.blog.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResouls(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin , admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion')
    resource_class = CategoriaResouls

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'apellidos']
    list_display = ('nombre', 'apellidos', 'estado', 'fecha_creacion')
    resource_class = CategoriaResouls

class PostAdmin(ImportExportModelAdmin , admin.ModelAdmin):
    resource_class = CategoriaResouls

class PreAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')
    resource_class = CategoriaResouls

class ProfesorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'apellidos', 'su_pre', 'fecha_creacion', 'fecha_nacimineto')
    resource_class = CategoriaResouls

class EstudianteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'apellidos', 'su_pre', 'su_profesor', 'fecha_creacion', 'fecha_nacimineto')
    resource_class = CategoriaResouls

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Pre_universitario, PreAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Estudiante, EstudianteAdmin)