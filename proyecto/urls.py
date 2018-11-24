from django.urls import path
from proyecto.views import *

urlpatterns = [
    path('', Index,name='index'),
    path('cursos/', CursoView.as_view(), name='cursos'),
]
