from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('actividades_formacion/', actividades_formacion, name='actividades_formacion'),
    path('info_carrera/', info_carrera, name='info_carrera'),
    path('informacion_didactica/', informacion_didactica, name='informacion_didactica'),
    path('<slug:slug>/', detallePost, name='detalle_post'),
]
