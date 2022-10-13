from django.contrib import admin
from .models import *

class ArtistaAdmin(admin.ModelAdmin):
	list_display = ('id_a', 'nombre_a', 'imagen_a', 'descripcion_a')
admin.site.register(Artista, ArtistaAdmin)

class RedsocialAdmin(admin.ModelAdmin):
	list_display = ('id_rs', 'id_a', 'nombre_rs', 'imagen_rs', 'url_rs')
admin.site.register(Redsocial, RedsocialAdmin)

class WallpaperAdmin(admin.ModelAdmin):
	list_display = ('id_w', 'nombre_w', 'imagen_w', 'id_a')
admin.site.register(Wallpaper, WallpaperAdmin)

class DatappAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombreapp', 'linkapp', 'keyapp')
admin.site.register(Datapp, DatappAdmin)