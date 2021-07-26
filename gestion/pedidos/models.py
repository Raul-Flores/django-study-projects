from django.db import models
from django.db.models.base import Model
from choices import sexos
# Create your models here.
class Docente(models.Model):
    apellido_paterno=models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido_materno=models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres= models.CharField(max_length=40, verbose_name='Nombres')
    fecha_nacimiento= models.DateField(verbose_name='fecha de nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='F')

    def nombre_completo(self):
        return f'{self.apellido_materno} {self.apellido_paterno}, {self.nombres}'
    def __str__(self):
        return self.nombre_completo()
    class Meta:
        verbose_name= 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        ordering=['apellido_paterno','-apellido_materno']
    
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveBigIntegerField()
    docente= models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return  f'{self.nombre} {self.creditos}'
