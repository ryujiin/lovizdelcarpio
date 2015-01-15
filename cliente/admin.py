from django.contrib import admin
from models import *

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','creado','get_usuario_id')

class DireccionAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','departamento','provincia','distrito','direccion')

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Comentario,ComentarioAdmin)