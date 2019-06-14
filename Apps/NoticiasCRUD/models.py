from django.db import models

# Create your models here.

class NoticiasModelo(models.Model):
    titulo=models.CharField(max_length=100)
    fecha=models.CharField(max_length=10)
    resumen=models.CharField(max_length=200) 
    detalle=models.CharField(max_length=500) 
    TIPO=(('N','Noticias'),('E','Eventos'))
    tipo=models.CharField(max_length=1, choices=TIPO, default='N')

    def __str__(self):
        cadena= self.titulo + " "
        cadena+= self.fecha + " "
        cadena+= self.resumen + " "
        cadena+= self.detalle + " "
        cadena+= self.tipoChoice
        return cadena