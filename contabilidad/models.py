from django.db import models
from catalogo.models import Producto
from material.models import Material,Planta

# Create your models here.
class Compras(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	material = models.ForeignKey(Material,blank=True,null=True)

class VentasMinorista(models.Model):
	producto = models.ForeignKey(Producto,blank=True,null=True)
	cantidad = models.PositiveIntegerField(default=1)

class CompraPlanta(models.Model):
	planta = models.ForeignKey(Planta,blank=True,null=True)
	fecha = models.DateTimeField(auto_now_add=True)
	cantidad = models.PositiveIntegerField(default=1)
	total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,editable=False)
	entregado = models.BooleanField(default=False)
	en_stock = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		self.total = self.cantidad * self.planta.precio
		if self.entregado==True:
			if self.en_stock==True:
				stock = self.planta.stock + self.cantidad
				self.planta.stock = stock
				self.planta.save()
				self.en_stock=False
		super(CompraPlanta, self).save(*args, **kwargs)