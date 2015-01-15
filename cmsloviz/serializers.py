from rest_framework import serializers
from models import *

class BloqueSerializer(serializers.ModelSerializer):
	seccion = serializers.CharField(read_only=True)
	template = serializers.CharField(read_only=True)
	class Meta:
		model = Bloque
		fields = ('id','nombre_interno','titulo','cuerpo','foto','template','link','css','paginas_mostrar','paginas_no_mostrar','seccion',)

class ImagensCarruselSerializers(serializers.ModelSerializer):
	class Meta:
		model = ImagenesCarrusel

class CarruselSerializer(serializers.ModelSerializer):
	seccion = serializers.CharField(read_only=True)
	imagenes_carrusel = ImagensCarruselSerializers (many=True)

	class Meta:
		model = Carrusel
		fields = ('id','titulo','nombre_interno','cuerpo','seccion','css','template','modelo','filtro','items_mostrar','tipo','imagenes_carrusel')

class PaginaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pagina
		fields=('id','titulo','slug','activo','cuerpo','css')

class LinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Link

class MenuSerialirzer(serializers.ModelSerializer):
	links =LinkSerializer(many=True)
	seccion = serializers.CharField(read_only=True)
	template = serializers.CharField(read_only=True)	
	class Meta:
		model = Menu
		fields = ('id','titulo','css','seccion','template','links')