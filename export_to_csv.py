#comando
#python manage.py runscript script_bda.py --verbosity 0

import csv
from proyecto.models import *

with open('datos/persona.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        persona = Persona.objects.create(cedula=row['cedula'],nombres=row['nombre'],apellidos=row['apellido'],direccion=row['direccion'],telefono=row['telefono'],email=row['email'])
        persona.save()

with open('datos/centro.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        centro = Centro.objects.create(nombre=row['nombre'],imagen=row['imagen'],telefono=row['telefono'],latitud=row['latitud'],longitud=row['longitud'],parroquia_id=row['parroquia_id'])
        centro.save()

with open('datos/servicios.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        servicios = Servicios.objects.create(nombre=row['nombre'],detalle=row['detalle'])
        servicios.save()

with open('datos/nino.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nino = Nino.objects.create(cedula=row['cedula'],nombres=row['nombre'],apellidos=row['apellido'],edad=row['edad'])
        nino.save()
