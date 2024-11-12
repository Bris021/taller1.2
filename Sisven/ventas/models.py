from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name= "Nombre",unique= True, blank=False)
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(max_length=2000, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
        
class Cliente (models.Model):
            nombre_cliente= models.CharField(max_length=50, verbose_name= "Nombre", unique=True, blank=False)
            apelllido_cliente= models.CharField(max_length=50, verbose_name= "Nombre", unique=True, blank=False)
            edad = models.IntegerField()
            correo = models.EmailField()
            domicilio = models.TextField(max_length=200, help_text="Escriba una indicacion de tu domicilio")

            def __srt__ (self):
                return f'{self.nombre_cliente}{self.apelllido_cliente}'
            
class Orden(models.Model):
        fecha = models.DateTimeField(auto_now_add=True)
        total = models.DecimalField(max_digits=4, decimal_places=2 )
        cliente = models.ForeignKey (Cliente, on_delete=models.RESTRICT)
        producto = models.ManyToManyField(Producto)

        def __str__(self):
              return f'Orden de {self.id} - Cliente'
