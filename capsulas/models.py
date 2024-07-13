from django.db import models

class Capsula(models.Model):
    id_capsula = models.IntegerField(primary_key=True)  
    nombre_capsula = models.CharField(max_length=50)
    descripcion_capsula = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'capsula'
        verbose_name_plural = 'capsulas'

    def __str__(self):
        return self.nombre_capsula