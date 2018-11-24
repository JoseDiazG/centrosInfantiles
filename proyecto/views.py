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
