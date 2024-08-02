from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()
    contenido =models.TextField()

    def __str__(self):
      return self.nombre
    
class Carta(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='carta/')

    def __str__(self):
        return self.titulo

from django.core.exceptions import ValidationError

class Galeria(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='galeria/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def clean(self):
        if self.imagen and self.video:
            raise ValidationError("Solo puedes elegir una imagen o un video, no ambos.")
        if not self.imagen and not self.video:
            raise ValidationError("Debes elegir al menos una imagen o un video.")

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    contacto = models.CharField(max_length=10, choices=[('email', 'Correo electrónico'), ('telefono', 'Teléfono')])

    def __str__(self):
        return f'{self.nombre} - {self.asunto}'
    
class cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    dni = models.CharField(max_length=15)
    telefono=models.CharField(max_length=20)
    direccion = models.TextField()
    def __str__(self):
        return self.usuario.username