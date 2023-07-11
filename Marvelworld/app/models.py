from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    img = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    

