from rest_framework import serializers
from models import *
from django.conf import settings

class ProductoListaSerializer(serializers.ModelSerializer):
	marca = serializers.CharField(read_only=True)
	color = serializers.CharField(read_only=True)
	thum = serializers.SerializerMethodField()
	class Meta:
		model=Producto
		fields=('id','nombre','full_name','slug','marca','color','categorias','thum')

	def get_thum(self,obj):
		imagen = obj.get_thum()
		return imagen.url
		
class ProductoVariacionSerializer(serializers.ModelSerializer):
	talla = serializers.CharField(read_only=True)
	precio_venta = serializers.SerializerMethodField('get_precio')
	precio = serializers.SerializerMethodField('get_precio_minorista')
	class Meta:
		model=ProductoVariacion
		fields =('id','talla','precio','oferta','precio_venta')

	def get_precio(self,obj):
		precio = obj.get_precio_venta()
		precio ="%0.2f" %(precio)
		return precio
		
	def get_precio_minorista(self,obj):
		precio = obj.precio_minorista
		precio ="%0.2f" %(precio)
		return precio


class ImgProductoSerializer(serializers.ModelSerializer):
	imagen = serializers.SerializerMethodField()
	imagen_medium = serializers.SerializerMethodField()
	imagen_thum = serializers.SerializerMethodField()
	class Meta:
		model = ProductoImagen
		fields =('imagen','imagen_medium','imagen_thum','orden')
	
	def get_imagen(self,obj):
		return obj.foto.url

	def get_imagen_medium(self,obj):
		url = obj.get_thum_medium().url
		return url

	def get_imagen_thum(self,obj):
		url = obj.get_thum().url
		return url

class ParienteSerialiezer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField('get_img_thum')
	class Meta:
		model = Producto
		fields = ('id','nombre','full_name','marca','thum','slug')

	def get_img_thum(self,obj):
		img = obj.get_thum().url
		return img

class ProductoSingleSereializer(serializers.ModelSerializer):
	categoria= serializers.CharField(read_only=True)
	estilo= serializers.CharField(read_only=True)
	color= serializers.CharField(read_only=True)
	variaciones = ProductoVariacionSerializer(many=True)
	imagenes_producto = ImgProductoSerializer(many=True)
	thum = serializers.SerializerMethodField('get_thum_img')
	parientes = ParienteSerialiezer(many=True)

	en_oferta = serializers.SerializerMethodField('get_oferta_lista')
	precio = serializers.SerializerMethodField('get_precio_lista')
	precio_venta = serializers.SerializerMethodField('get_precio_descuento')
	genero = serializers.SerializerMethodField()
	relacionados = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

	class Meta:
		model = Producto
		fields = ('id','nombre','full_name','marca','genero','categoria','estilo','color','slug','activo','descripcion','thum',
				'en_oferta','precio','precio_venta',
				'imagenes_producto','variaciones','parientes','video','detalles','relacionados')

	def get_thum_img(self,obj):
		thum = obj.get_thum().url
		return thum

	def get_oferta_lista(self,obj):
		return obj.get_en_oferta()

	def get_precio_lista(self,obj):
		precio= obj.get_precio_lista()
		return precio

	def get_precio_descuento(self,obj):
		precio= obj.get_precio_oferta_lista()
		return precio

	def get_genero(self,obj):
		genero = obj.categoria.genero.nombre
		return genero

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria

class ColoresSerializers(serializers.ModelSerializer):
	filtro = serializers.SerializerMethodField()	
	class Meta:
		model = Color
		fields=('nombre','slug','filtro')

	def get_filtro(self,obj):
		return 'color'

class TallaSerializers(serializers.ModelSerializer):
	filtro = serializers.SerializerMethodField()

	class Meta:
		model = Talla
		fields=('nombre','slug','filtro')

	def get_filtro(self,obj):
		return 'talla'
