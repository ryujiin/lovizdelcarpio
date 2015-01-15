from django.db import models
from django.template.defaultfilters import slugify
from catalogo.models import Categoria


class Menu(models.Model):
	titulo = models.CharField(max_length=120,blank=True,null=True)
	nombre_interno = models.CharField(max_length=120,unique=True)
	seccion = models.ForeignKey('SeccionesPagina',blank=True,null=True)
	css = models.CharField(max_length=120,blank=True,null=True)
	pagina = models.ForeignKey('Pagina',blank=True,null=True,related_name='menus')
	template = models.ForeignKey('TemplatePagina',blank=True,null=True)

	def __unicode__(self):
		return self.nombre_interno

class Link(models.Model):
	titulo = models.CharField(max_length=120,blank=True,null=True)
	css = models.CharField(max_length=120,blank=True,null=True)
	menu = models.ForeignKey('Menu',related_name='links')
	icono = models.CharField(max_length=120,blank=True,null=True)
	enlace = models.CharField(max_length=120,blank=True,null=True)
	peso = models.PositiveIntegerField(default=0)

	class Meta:
		unique_together = ('menu','peso')
		ordering = ['peso']

	def __unicode__(self):
		return '%s de %s' %(self.titulo,self.menu)

def url_imagen_pr(self,filename):
	url = "bloque/imagen/%s" % (filename)
	return url

class Bloque(models.Model):
	titulo = models.CharField(max_length=120,blank=True,null=True)
	nombre_interno = models.CharField(max_length=120,unique=True)
	paginas_mostrar = models.ManyToManyField('Pagina',blank=True,null=True,related_name='bloques')
	paginas_no_mostrar = models.ManyToManyField('Pagina',blank=True,null=True,related_name='bloques_excluidos')
	activo = models.BooleanField(default=True)
	cuerpo = models.TextField(blank=True,null=True)
	seccion = models.ForeignKey('SeccionesPagina',blank=True,null=True)
	foto = models.ImageField(upload_to=url_imagen_pr,blank=True,null=True)
	template = models.ForeignKey('TemplatePagina',blank=True,null=True)
	link = models.CharField(max_length=120,blank=True,null=True)
	css = models.CharField(max_length=120,blank=True,null=True)

	def __unicode__(self):
		return "%s" %self.nombre_interno

	def save(self, *args, **kwargs):
		self.nombre_interno = slugify(self.nombre_interno)
		super(Bloque, self).save(*args, **kwargs)

class Carrusel(models.Model):
	TIPO=(('modelo','model'),('imagenes','imagenes'))
	paginas_mostrar = models.ManyToManyField('Pagina',blank=True,null=True,related_name='carrusel')
	paginas_no_mostrar = models.ManyToManyField('Pagina',blank=True,null=True,related_name='carrusel_excluido')
	titulo = models.CharField(max_length=120,blank=True,null=True)
	nombre_interno = models.CharField(max_length=120,unique=True,blank=True,null=True)
	tipo = models.CharField(max_length=100,choices=TIPO,blank=True,null=True)
	activo = models.BooleanField(default=True)
	cuerpo = models.TextField(blank=True,null=True)
	seccion = models.ForeignKey('SeccionesPagina',blank=True,null=True)
	modelo = models.CharField(max_length=120,blank=True,null=True)
	filtro=models.CharField(max_length=120,blank=True,null=True)
	items_mostrar=models.CharField(max_length=120,blank=True,null=True)
	css = models.CharField(max_length=120,blank=True,null=True)
	template = models.ForeignKey('TemplatePagina',blank=True,null=True)
	

	def save(self, *args, **kwargs):
		if not self.nombre_interno:
			self.nombre_interno ="%s %s" %(self.pagina,self.titulo)
		self.nombre_interno = slugify(self.nombre_interno)
		super(Carrusel, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre_interno
def url_imagen_carrusel(self,filename):
	url = "carrusel/imagen/%s" % (filename)
	return url

class ImagenesCarrusel(models.Model):
	imagen = models.ImageField(upload_to=url_imagen_carrusel,blank=True,null=True)
	carrusel = models.ForeignKey(Carrusel,blank=True,null=True,related_name='imagenes_carrusel')
	titulo = models.CharField(max_length=130,blank=True,null=True)
	order = models.PositiveIntegerField(default=1)	

class Pagina(models.Model):
	titulo = models.CharField(max_length=120,blank=True,null=True)
	slug = models.CharField(max_length=120,unique=True,blank=True,null=True)
	activo = models.BooleanField(default=True)
	cuerpo = models.TextField(blank=True,null=True)
	template = models.ForeignKey('TemplatePagina',blank=True,null=True)
	css = models.CharField(max_length=120,blank=True,null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.slug)
		super(Pagina, self).save(*args, **kwargs)

	def get_num_bloques(self):
		num = Bloque.objects.filter(pagina=self.pk).count()
		return num

	def get_num_carrusel(self):
		num = Bloque.objects.filter(pagina=self.pk).count()
		return num

	def __unicode__(self):
		return "%s - %s" %(self.titulo,self.slug)

class SeccionesPagina(models.Model):
	nombre = models.CharField(max_length=120)
	nombre_interno = models.CharField(max_length=120,unique=True,blank=True,null=True)

	def __unicode__(self):
		return self.nombre

	def save(self,*args,**kwargs):
		if not self.nombre_interno:
			self.nombre_interno = self.nombre
		self.nombre_interno=slugify(self.nombre_interno)
		super(SeccionesPagina, self).save(*args, **kwargs)

class TemplatePagina(models.Model):
	nombre = models.CharField(max_length=120)
	nombre_interno = models.CharField(max_length=120,unique=True,blank=True,null=True)

	def __unicode__(self):
		return self.nombre

	def save(self,*args,**kwargs):
		if not self.nombre_interno:
			self.nombre_interno = self.nombre
		self.nombre_interno=slugify(self.nombre_interno)
		super(TemplatePagina, self).save(*args, **kwargs)