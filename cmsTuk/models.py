from cms.models import CMSPlugin
from django.db import models

class botonClass(models.Model):
    clase = models.CharField(max_length=255)
    def __unicode__(self):
        return self.clase

class botonIcono(models.Model):
    icono = models.CharField(max_length=255)
    def __unicode__(self):
        return self.icono

class cabezeraPlugin(CMSPlugin):
    logo    = models.ImageField(upload_to='productos', verbose_name='Imagen')
    titulo  = models.CharField(max_length=255)
    boton1  = models.BooleanField(verbose_name="Boton 1",
        help_text='Boton en Cabezera, se pocicionara a la izquierda')
    clase1  = models.ForeignKey('botonClass', related_name='boton1_clase', verbose_name="Clase",
        null=True, blank=True)
    icono1  = models.ForeignKey('botonIcono', related_name='boton1_icono', verbose_name="Icono",
        null=True, blank=True)
    texto1  = models.CharField(max_length=20, verbose_name="Texto",
        null=True, blank=True, help_text='Use un texto corto para no saturar la cabezera')
    href1   = models.CharField(max_length=255, default='#',
        null=True, blank=True)
    boton2  = models.BooleanField(verbose_name="Boton 2",
        help_text='Segundo boton en Cabezera, recomendamos 2 y no mas de 3 botones en cabezera')
    clase2  = models.ForeignKey('botonClass', related_name='boton2_clase', verbose_name="Clase",
        null=True, blank=True)
    icono2  = models.ForeignKey('botonIcono', related_name='boton2_icono', verbose_name="Icono",
        null=True, blank=True)
    texto2  = models.CharField(max_length=20, verbose_name="Texto",
        null=True, blank=True)
    href2   = models.CharField(max_length=255, default='#',
        null=True, blank=True)
    boton3  = models.BooleanField(verbose_name="Boton 3",
        help_text='Tercier boton en Cabezera, es posible que sea demaciado contenido para la cabezera')
    clase3  = models.ForeignKey('botonClass', related_name='boton3_clase', verbose_name="Clase",
        null=True, blank=True)
    icono3  = models.ForeignKey('botonIcono', related_name='boton3_icono', verbose_name="Icono",
        null=True, blank=True)
    texto3  = models.CharField(max_length=20, verbose_name="Texto",
        null=True, blank=True)
    href3   = models.CharField(max_length=255, default='#',
        null=True, blank=True)
    def __unicode__(self):
      return self.titulo
