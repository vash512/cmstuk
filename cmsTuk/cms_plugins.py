from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsTuk.models import cabezeraPlugin as cabezeraPluginModel
from django.utils.translation import ugettext as _

class CabezeraPlugin(CMSPluginBase):
    model = cabezeraPluginModel # Model where data about this plugin is saved
    name = _("Cabezera Tuk Tuk") # Name of the plugin
    render_template = "plugins/cabezeraTukTuk.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(CabezeraPlugin) # register the plugin