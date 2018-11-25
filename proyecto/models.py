from django.db import models

# Create your models here.
class Persona(models.Model):
    cedula = models.IntegerField()
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.CharField(max_length=60)
    def __str__(self):
       return 'id: '+ str(self.id)+' - '+ self.nombres +' '+ self.apellidos

class Representante(models.Model):
    cant_hijos = models.IntegerField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Docente(models.Model):
    titulo = models.CharField(max_length=45)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Nino(models.Model):
    cedula = models.IntegerField()
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()

class Detalle_Representante(models.Model):
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE)

class Sala(models.Model):
    num_sala = models.IntegerField()
    capacidad = models.IntegerField()
    descripcion = models.CharField(max_length=40)

class Provincia(models.Model):
    nombre = models.CharField(max_length=45)

class Canton(models.Model):
    nombre = models.CharField(max_length=45)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

class Parroquia(models.Model):
    nombre = models.CharField(max_length=45)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)


class Centro(models.Model):
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=150)
    telefono = models.IntegerField()
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    direccion = models.CharField(max_length=100)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

class Curso(models.Model):
    periodo = models.DateField(auto_now=False)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

class Alumno(models.Model):
    descripcion = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE)

class Servicios(models.Model):
    nombre = models.CharField(max_length=45)
    detalle = models.CharField(max_length=45)

class Centro_Servicios(models.Model):
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    servicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)



#ya esta la bd creada

    #estan mal definidos los valores de tu tabla gay tienes que corregir
    #el id en django nunca se declara se crea por defecto pilas con eso
