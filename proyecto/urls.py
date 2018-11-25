from django.urls import path
from proyecto.views import *

urlpatterns = [
    path('', Index,name='index'),
    path('cursos/', CursoView.as_view(), name='cursos'),
    path('personas/', PersonaView.as_view(), name='personas'),
    path('centros/', CentroView.as_view(), name='centros'),
    path('detalle-centro/<int:id>/', CentroDetalleView.as_view(), name='detalle-centro'),
    path('detalle-curso/<int:id>/', CursoDetalleView.as_view(), name='detalle-curso'),
]
