from django.db import models

# Create your models here.
class software(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'softwares'

class depa(models.Model):
    nombre = models.CharField(max_length=100)
