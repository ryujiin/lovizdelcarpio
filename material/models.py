from django.db import models
from catalogo.models import Producto,Talla,Color

# Create your models here.

class Material(models.Model):
	nombre = models.CharField(max_length=100)
	unidad_compra = models.CharField(max_length=100,blank=True,null=True)
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	fecha = models.DateTimeField(auto_now_add=True)
	foto = models.ImageField(upload_to='uploads/materiales/',blank=True,null=True)

class MaterialesProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='materiales')
	material = models.ForeignKey('Material',blank=True,null=True)
	cantidad_docena = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	unidad_medida = models.CharField(max_length=100,blank=True, null=True)
	cantidad_par = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	precio_docena = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

	def save(self, *args, **kwargs):
		self.unidad_compra = self.material.unidad_compra
		super(MaterialesProductos, self).save(*args, **kwargs)

class Planta(models.Model):
	TIPO=(('Mujer-001','Mujer-001'),('Hombre-002','Hombre-002'))
	tipo = models.CharField(max_length=100,blank=True,null=True,choices=TIPO)
	nombre = models.CharField(max_length=100,blank=True,null=True)
	talla = models.ForeignKey(Talla,blank=True,null=True)
	color = models.ForeignKey(Color,blank=True,null=True)
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	stock = models.PositiveIntegerField(default=0)
	total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

	def save(self, *args, **kwargs):
		self.nombre = ('%s-%s,%s') %(self.tipo,self.color.nombre,self.talla.nombre)
		self.total = self.precio*self.stock
		super(Planta, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre