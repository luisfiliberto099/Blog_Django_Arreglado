from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=100, null= False, blank=False, verbose_name='Nombre de la categoria')
    estado = models.BooleanField(verbose_name='Categoría Activada/Categoría Desactivada', default=True)
    fecha_creacion = models.DateField(verbose_name='Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null= False, blank=False, verbose_name='Nombre de la Autor')
    apellidos = models.CharField(max_length=255, null= False, blank=False, verbose_name='Apellidos de la Autor')
    estado = models.BooleanField(verbose_name='Autor Activo/No Activo', default=True)
    fecha_creacion = models.DateField(verbose_name='Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellidos)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=90, blank=False, null=False, verbose_name='Titulo')
    slug = models.CharField(max_length=100, blank=False, null=False, verbose_name='Slugs')
    descripcion = models.CharField(max_length=100, blank=False, null=False, verbose_name='Descripción')
    contenido = RichTextField(verbose_name='Contenido')
    imagen = models.URLField(max_length=9999999 ,blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True ,verbose_name='Publicado/No Publicado')
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class Pre_universitario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=255, null= False, blank=False, verbose_name='Nombre del instituto preuniversitario')
    fecha_creacion = models.DateField(verbose_name='Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Pre_universitario'
        verbose_name_plural = 'Pre_universitarios'

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nombre del profesor')
    apellidos = models.CharField(max_length=255, null=False, blank=False, verbose_name='Apellidos del profesor')
    su_pre = models.ForeignKey(Pre_universitario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(verbose_name='Fecha de creación del registro', auto_now=False, auto_now_add=True)
    fecha_nacimineto = models.DateField(verbose_name='Fecha de nacimiento', auto_created=False)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nombre del profesor')
    apellidos = models.CharField(max_length=255, null=False, blank=False, verbose_name='Apellidos del profesor')
    su_pre = models.ForeignKey(Pre_universitario, on_delete=models.CASCADE)
    su_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(verbose_name='Fecha de creación del registro', auto_now=False, auto_now_add=True)
    fecha_nacimineto = models.DateField(verbose_name='Fecha de nacimiento', auto_created=False)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.nombre