from django.db import models

# Create your models here.
class netdevice(models.Model):
    id = models.AutoField(primary_key=True)
    direccionip = models.CharField(max_length=40)
    protocolo = models.CharField(max_length=15)
    puerto = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.direccionip}'