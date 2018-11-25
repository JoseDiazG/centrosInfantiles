from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.template import loader
from django.views.generic import TemplateView
from proyecto.models import *



def Index(request):
    template_name = 'proyecto/index.html'
    return HttpResponse('output asa')

class CursoView(TemplateView):
    template_name = 'proyecto/cursos.html'
    def get(self,request):
        cursos = Curso.objects.all()
        return render(request, self.template_name ,{'cursos': cursos})

class PersonaView(TemplateView):
    template_name = 'proyecto/personas.html'
    def get(self,request):
        personas = Persona.objects.all()
        return render(request, self.template_name ,{'personas': personas})

class CentroView(TemplateView):
    template_name = 'proyecto/centros.html'
    def get(self,request):
        centros = Centro.objects.all()
        return render(request, self.template_name ,{'centros': centros})

class CentroDetalleView(TemplateView):
    template_name = 'proyecto/detalle-centro.html'
    def get(self,request, id):
        centro = Centro.objects.get(pk=id)
        cursos = Curso.objects.filter(centro_id=id)
        servicios = Centro_Servicios.objects.filter(centro_id=id)
        args = {'centro': centro,'cursos':cursos,'servicios':servicios}
        return render(request, self.template_name , args)

class CursoDetalleView(TemplateView):
    template_name = 'proyecto/detalle-curso.html'
    def get(self,request, id):
        curso = Curso.objects.get(pk=id)
        alumnos = Alumno.objects.filter(curso_id=id)
        args = {'curso': curso,'alumnos':alumnos}
        return render(request, self.template_name , args)
