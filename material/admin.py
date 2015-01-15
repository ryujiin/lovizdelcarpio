from django.contrib import admin
from models import *
# Register your models here.
class PlantaAdmin(admin.ModelAdmin):
	list_display = ('nombre','precio','stock','total')


admin.site.register(Material)
admin.site.register(MaterialesProductos)
admin.site.register(Planta,PlantaAdmin)