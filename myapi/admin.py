from django.contrib import admin
from .models import *

class ArtistaAdmin(admin.ModelAdmin):
	list_display = ('id_a', 'nombre_a', 'imagen_a', 'descripcion_a')
admin.site.register(Artista, ArtistaAdmin)

class RedsocialAdmin(admin.ModelAdmin):
	list_display = ('id_a', 'id_rs', 'nombre_rs', 'imagen_rs', 'url_rs')
admin.site.register(Redsocial, RedsocialAdmin)

#class RedsocialArtistaAdmin(admin.ModelAdmin):
#	list_display = ('id_rs', 'id_a', 'url_rsa', 'imagen_rs')
#admin.site.register(RedsocialArtista, RedsocialArtistaAdmin)

class WallpaperAdmin(admin.ModelAdmin):
	list_display = ('id_w', 'nombre_w', 'imagen_w', 'id_a')
admin.site.register(Wallpaper, WallpaperAdmin)

class DatappAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulomapp', 'mensajeapp', 'linkapp', 'keyapp', 'iconapp')
admin.site.register(Datapp, DatappAdmin)