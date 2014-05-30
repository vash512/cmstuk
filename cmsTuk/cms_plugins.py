from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from cms.plugin_pool import plugin_pool
from cmsTuk.models import headerPlugin as headerPluginModel
from cmsTuk.models import cabezeraPlugin as cabezeraPluginModel
from cmsTuk.models import socialmediaPlugin as socialmediaPluginModel
from django.utils.translation import ugettext as _

class HeaderPlugin(CMSPluginBase):
    model = headerPluginModel # Model where data about this plugin is saved
    name = _("Tuk Tuk <Header>") # Name of the plugin
    render_template = "plugins/cabezeraTukTuk.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance},)
        return context

class CabezeraPlugin(CMSPluginBase):
    model = cabezeraPluginModel # Model where data about this plugin is saved
    name = _("Tuk Tuk Cabezera") # Name of the plugin
    render_template = "plugins/subHeadTukTuk.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        mess=''
        if 'eviarCorreo' in context['request'].POST and instance.destino:
            mensaje = context['request'].POST.get('msg','')
            if instance.plantilla:
                htmly = get_template('email/plantilla1.html')
                d = Context({'email':mensaje})
                html_content = htmly.render(d)
            else:
                html_content = 'esta persona esta interesada en tu pagina: %s'%mensaje

            asunto='Hola'
            para=[instance.destino.correo]
            #para=['chipgirl_g87@hotmail.com', 'fa.hikariangel@gmail.com',
            #'fhy_hdez@yahoo.com.mx', 'xtornasol512@gmail.com', 'jesua_cb@yahoo.com.mx','malu__ag@hotmail.com',
            #'malu.ag@gmail.com', 'phyrox.vash512@gmail.com', 'nextcase_jesus001@hotmail.com']
            for name in para:
                d = Context({'nombre':name})
                email = EmailMessage(asunto+' '+name, html_content, to=[name])
                email.content_subtype = "html"
                mess= email.send()

        context.update({'instance':instance, 'mess':mess})
        return context

class SocialMediaPlugin(CMSPluginBase):
    model = socialmediaPluginModel # Model where data about this plugin is saved
    name = _("Tuk Tuk SocialMedia") # Name of the plugin
    render_template = "plugins/socialmediaTukTuk.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance},)
        return context

plugin_pool.register_plugin(CabezeraPlugin) # register the plugin
plugin_pool.register_plugin(HeaderPlugin)
plugin_pool.register_plugin(SocialMediaPlugin)