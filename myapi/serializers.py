# serializers.py
from rest_framework import serializers
from myapi.models import *

class ArtistaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artista
		fields = ('id_a', 'nombre_a', 'imagen_a', 'descripcion_a')

class WallpaperSerializer(serializers.HyperlinkedModelSerializer):
	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
	class Meta:
		model = Wallpaper
		fields = ('id_w', 'id_a', 'nombre_w', 'imagen_w')

class RedsocialSerializer(serializers.HyperlinkedModelSerializer):
	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
	class Meta: 
		model = Redsocial
		fields = ('id_rs', 'id_a', 'nombre_rs', 'imagen_rs', 'url_rs')

class DatappSerializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = Datapp
		fields = ('id', 'nombreapp', 'linkapp', 'keyapp')