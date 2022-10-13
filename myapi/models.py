from django.db import models

class Artista(models.Model):
	id_a = models.BigAutoField(primary_key=True)
	nombre_a = models.CharField(max_length=60)
	imagen_a = models.ImageField(null=True, blank=True)
	descripcion_a = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre_a

	@property
	def imageURL(self):
		try:
			url = self.imagen_a.url
		except:
			url = ''
		return url

class Redsocial(models.Model):
	id_rs = models.BigAutoField(primary_key=True)
	id_a = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)
	nombre_rs = models.CharField(max_length=20)
	imagen_rs = models.ImageField(null=True, blank=True)
	url_rs = models.CharField(max_length=150)
	def __str__(self):
		return self.nombre_rs

	@property
	def imageURL(self):
		try:
			url = self.imagen_rs.url
		except:
			url = ''
		return url

class Wallpaper(models.Model):
	id_w = models.BigAutoField(primary_key=True)
	id_a = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)
	nombre_w = models.CharField(max_length=100)
	imagen_w = models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.nombre_w

	@property
	def imageURL(self):
		try:
			url = self.imagen_w.url
		except:
			url = ''
		return url

class Datapp(models.Model):
	nombreapp = models.CharField(max_length=20)
	linkapp = models.CharField(max_length=150)
	keyapp = models.CharField(max_length=100)
	def __str__(self):
		return self.nombreapp