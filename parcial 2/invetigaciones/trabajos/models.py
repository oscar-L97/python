from django.db import models
from django.conf import settings


# Create your models here.
class Trabajo(models.Model):
    COMPUTACIONALES = 'CC'
    TIERRA = 'CT'
    NATURALES = 'CN'
    SOCIALES = 'CS'
    MEDICAS = 'CM'
    CATEGORIAS=(
        (COMPUTACIONALES, 'Ciencias Computacionales'),
        (TIERRA, 'Ciencias de la Tierra'),
        (NATURALES, 'Ciencias Naturales'),
        (SOCIALES, 'Ciencias Sociales'),
        (MEDICAS, 'Ciencias Medicas'),
    )
    documento = models.FileField(upload_to='documents/')
    categoria = models.CharField(max_length=2,choices=CATEGORIAS,default=COMPUTACIONALES)
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    timestamp=models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
