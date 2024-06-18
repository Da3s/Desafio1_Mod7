from django.db import models

# Create your models here.

class Tarea(models.Model):
    descripcion = models.CharField(default='')
    eliminada = models.BooleanField(default=False)
    
class Subtarea(models.Model):
    descripcion = models.CharField(default='')
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE) # Se declara aqui la clave foranea que viene desde Tarea, en este caso el ID