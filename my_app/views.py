from django.views.generic import TemplateView
import my_app.demo_software.main as demo
import json

drugstone_settings = {
    'groups': json.dumps({'nodeGroups': {'Gene': {'type':'Gene','color':'#999999','groupName':'Genes','shape':'ellipse'}}}),
    'config': json.dumps({'identifier': 'symbol', 'title': 'Drugst.One django demo', 'autofillEdges': True}),
    'network': []
}

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parameter = self.kwargs.get('parameter', False)
        if parameter:
            genes = demo.run(int(parameter))
            context['gene_list'] = genes
            nodes = [{'id':gene, 'group': 'Gene'} for gene in genes]
            drugstone_settings['network'] = json.dumps({'nodes': nodes})
            context.update(drugstone_settings)
        return context
