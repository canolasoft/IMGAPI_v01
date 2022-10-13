from rest_framework import viewsets
import django_filters
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import(ListCreateAPIView)

# Consulta 0: dame los datos de la app
class DatappViewSet(viewsets.ModelViewSet):
	queryset = Datapp.objects.all()
	serializer_class = DatappSerializer

# index de prueba (muestra todos los artistas)
def index(request):
	artistas = Artista.objects.all().order_by('nombre_a')
	context = {'artistas':artistas}
	return render(request, "landing/index.html", context)

# Consulta 1: dame todos los Artistas
class ArtistasViewSet(viewsets.ModelViewSet):
	queryset = Artista.objects.all().order_by('nombre_a')
	serializer_class = ArtistaSerializer

# Consulta 2: dame todos los Wallpapers de un Artista
class WallpaperSerializer(ListCreateAPIView):
	serializer_class = WallpaperSerializer

	def get_queryset(self):
		id_a = self.request.GET.get('id')
		wallpapers = Wallpaper.objects.filter(id_a__id_a = id_a)
		return wallpapers

# Consulta 3: dame los datos de un Artista
class ArtistaViewSet(viewsets.ModelViewSet):
	serializer_class = ArtistaSerializer

	def get_queryset(self):
		id_a = self.request.GET.get('id')
		return Artista.objects.filter(id_a = id_a)

# Consulta 4: dame las Redes de un Artista
class RedsocialSerializer(ListCreateAPIView):
	serializer_class = RedsocialSerializer

	def get_queryset(self):
		id_a = self.request.GET.get('id')
		redesociales = Redsocial.objects.filter(id_a__id_a = id_a)
		return redesociales
