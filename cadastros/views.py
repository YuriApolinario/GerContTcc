from django.views.generic.edit import CreateView

from .models import Estado, Cidade, Servico, Empresa, Propriedade

from django.urls import reverse_lazy

class EstadoCreate(CreateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CidadeCreate(CreateView):
    models = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ServicoCreate(CreateView):
    model = Servico
    fields = ['descricao_servico', 'valor']
    template_name ='cadastros/form.html'
    success_url = reverse_lazy('index')

class EmpresaCreate(CreateView):
    model = Empresa
    fields =  ['razao_social', 'cnpj', 'inscricao_estadual', 'endereco', 'minha_empresa']
    template_name ='cadastros/form.html'
    success_url = reverse_lazy('index')

class PropriedadeCreate(CreateView):
    model = Propriedade
    fields = ['nome_propriedade', 'endereco', 'area_propriedade', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
