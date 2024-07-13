from django.db import models
from autenticacion.models import Usuario_Registro

class Solicitudes_Epps(models.Model):
    id_solicitudEpps = models.AutoField(primary_key=True)
    nombreEpps = models.CharField(max_length=100, verbose_name='Nombre del EPP')
    fecha_realizarEP = models.DateField(verbose_name='Fecha de Emisión')
    descripcionEpps = models.CharField(max_length=300, verbose_name='Denominación - (Especifique adecuadamente talla y tipo de vestimenta para todos los EPPs)')
    tipo_materialEpps = models.CharField(max_length=300, choices=[('unitario', 'Unitario'), ('más de un elemento', 'Más de un elemento')], verbose_name='Tipo de material de Epps')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_usuario = models.ForeignKey(Usuario_Registro, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=30, choices=Usuario_Registro.TIPO_USUARIO_CHOICES)

    class Meta:
        verbose_name = 'Solicitud de EPP'
        verbose_name_plural = 'Solicitudes de EPPs'

    def __str__(self):
        return self.nombreEpps

class Solicitudes_Retiro(models.Model):
    id_solicitudRetiro = models.AutoField(primary_key=True)
    nombre_retiro = models.CharField(max_length=100, verbose_name='Material Retiro')
    fecha_realizarR = models.DateField(verbose_name='Fecha de Emisión')
    descripcionRetiro = models.CharField(max_length=300, verbose_name='Denominación - (Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de retiro)')
    cantidadRetiro = models.IntegerField(verbose_name='Cantidad a retirar')
    tipo_materialRetiro = models.CharField(max_length=10, choices=[('fardo', 'Fardo'), ('kilo', 'Kilo'), ('bolsa', 'Bolsa'), ('un', 'UN')], verbose_name='Tipo de material de retiro')
    patente = models.CharField(max_length=6, verbose_name='Patente del vehículo Ej:ABCD12')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_usuario = models.ForeignKey(Usuario_Registro, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=30, choices=Usuario_Registro.TIPO_USUARIO_CHOICES)

    class Meta:
        verbose_name = 'Solicitud de retiro'
        verbose_name_plural = 'Solicitudes de retiros'

    def __str__(self):
        return self.nombre_retiro


class Solicitudes_Tolva(models.Model):
    id_solicitudTolva = models.AutoField(primary_key=True)
    nombre_tolva = models.CharField(max_length=100, verbose_name='Nombre de Tolva')
    fecha_realizarT = models.DateField(verbose_name='Fecha de Emisión')
    descripcionTolva = models.CharField(max_length=300, verbose_name='Denominación - (Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de tolva)')
    tipo_retiro_pedido = models.CharField(max_length=100, choices=[
        ('retirar compactadora', 'Retirar Compactadora'),
        ('retirar tolva de vidrio', 'Retirar Tolva de Vidrio'),
        ('retirar tolva abierta', 'Retirar Tolva Abierta'),
        ('pedir tolva abierta', 'Pedir Tolva Abierta'),
        ('pedir tolva grande', 'Pedir Tolva Grande'),
        ('pedir tolva mediana', 'Pedir Tolva Mediana'),
        ('pedir tolva pequeña', 'Pedir Tolva Pequeña'),
    ], verbose_name='Retiro o Pedidos de Tolva')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_usuario = models.ForeignKey(Usuario_Registro, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=30, choices=Usuario_Registro.TIPO_USUARIO_CHOICES)

    class Meta:
        verbose_name = 'Solicitud de Tolva'
        verbose_name_plural = 'Solicitudes de Tolvas'

    def __str__(self):
        return self.nombre_tolva