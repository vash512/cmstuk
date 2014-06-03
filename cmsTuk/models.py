# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from inline_ordering.models import Orderable

class botonClass(models.Model):
    clase = models.CharField(max_length=255)
    def __unicode__(self):
        return self.clase

class botonIcono(models.Model):
    icono = models.CharField(max_length=255)
    def __unicode__(self):
        return self.icono

class plantillasCorreo(models.Model):
    nombre = models.CharField(max_length=255)
    html   = models.FileField(upload_to='email/plantillas', verbose_name='Archivo HTML',
        help_text="Plantilla en Html para los correos electronicos")
    def __unicode__(self):
        return self.nombre

class correo(models.Model):
    correo=models.CharField(max_length=255)
    def __unicode__(self):
        return self.correo

class headerPlugin(CMSPlugin):
    logo    = models.ImageField(upload_to='cms/headers', verbose_name='Imagen')
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


class cabezeraPlugin(CMSPlugin):
    titulo = models.CharField(max_length=255)
    encabezado  = models.TextField(verbose_name="Encabezado")
    fondo    = models.ImageField(upload_to='cms/cabezera', verbose_name='Fondo',
        null=True, blank=True)
    correo = models.BooleanField(verbose_name="Seccion de Correo")
    destino = models.ForeignKey( 'correo', blank=True, null=True,
        help_text='Correo de destino')
    plantilla = models.ForeignKey('plantillasCorreo', blank=True, null=True,
        help_text='Plantilla de Correo, si no selecciona ninguna, se enviara un correo con Estructura simple')
    placeholderEmail = models.CharField(max_length= 255, default='Tu dirección de e@mail.com para informarte',
        null=True, blank=True)
    subtexto = models.TextField(verbose_name="Texto Secundario", null=True,
        blank=True, help_text='Forma parte del Correo.')
    def __unicode__(self):
        return self.titulo

class idioma(models.Model):
    idioma =  models.CharField(max_length=255)
    codigo =  models.CharField(max_length=5, verbose_name="codigo del idioma",
     help_text='ejemplo es, en')
    def __unicode__(self):
        return self.idioma

class socialmediaPlugin(CMSPlugin):
    videoYT = models.CharField(max_length=255, verbose_name="Url de Video",
        null=True, blank=True,
        help_text='Url de video o lista de videos en YouTube.com')
    canal =  models.CharField(max_length=255, verbose_name="Canal de Youtube", null=True, blank=True,
        help_text='Nombre del canal de YouTube')
    twitter = models.CharField(max_length=255, verbose_name="Cuenta de Twitter",
        null=True, blank=True, help_text='Nombre de la cuenta de Twitter')
    twitterText = models.CharField(max_length=110, verbose_name="Texto del Twitt", null=True,
        blank=True, help_text='oracion con la que se twitteara')
    via    = models.CharField(max_length=30, null=True, blank=True,
        help_text='Via Twitter')
    idioma = models.ForeignKey('idioma', help_text='Idioma Twitter', null=True, blank=True)
    facebook = models.CharField(max_length=255, verbose_name="Url de facebook", null=True, blank=True,
        help_text='Url de pagina de facebook')
    foursquare = models.CharField(max_length=255, verbose_name="Url de foursquare",
        null=True, blank=True)
    googleplus = models.CharField(max_length=255, verbose_name="Url de googleplus",
        null=True, blank=True)
    def __unicode__(self):
        return self.canal

class carroManual(CMSPlugin):
    titulo      = models.CharField(max_length=255, null=True, blank=True)
    texto       = models.TextField(verbose_name="Texto principal", null=True,
                  blank=True)
    mostrar     = models.BooleanField(verbose_name="Cabezera", default=True,
                  help_text="Mostrar los Datos de cabezera (Titulo y Texto)" )
    comentario  = models.BooleanField(verbose_name="Formulario de Contacto", 
                  help_text="Mostrar el formulario de Contacto al Final", default=True)
    tituloF     = models.CharField(verbose_name="Titulo del formulario",max_length=255,
                  null=True, blank=True)
    textoF      = models.TextField(verbose_name="Texto del Formulario", null=True,
                  blank=True)
    tituloBoton = models.CharField(verbose_name="Texto del boton",max_length=255,
                  null=True, blank=True)

class bloqueCarroM(Orderable):
    carroM = models.ForeignKey('carroManual',
                  null=True, blank=True)
    titulo = models.CharField(max_length=255, null=True, blank=True,
             help_text="Puede ser opcional" )
    texto  = models.TextField(verbose_name="Texto principal")