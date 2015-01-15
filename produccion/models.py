from django.db import models
from catalogo.models import Talla,Color,Producto
# Create your models here.

class Planta(models.Model):
	TIPO=(('Mujer-001','Mujer-001'),('Hombre-002','Hombre-002'))
	tipo = models.CharField(max_length=100,blank=True,null=True,choices=TIPO)
	nombre = models.CharField(max_length=100,blank=True,null=True)
	talla = models.ForeignKey(Talla,blank=True,null=True)
	color = models.ForeignKey(Color,blank=True,null=True)
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	stock = models.PositiveIntegerField(default=0)

	def save(self, *args, **kwargs):
		self.nombre = ('%s-%s,%s') %(self.tipo,self.color.nombre,self.talla.nombre)
		super(Planta, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre