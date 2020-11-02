from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *

from django.views.generic.list import ListView

from django.urls import reverse_lazy

class EstadoCreate(CreateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CidadeCreate(CreateView):
    model = Cidade
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

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome', 'endereço', 'cpf', 'rg', 'sexo', 'telefone', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ContratoCreate(CreateView):
    model = Contrato
    fields = ['servico', "propriedade", "data_inicial", "data_final", "registrado_por", "registrado_em", "contratante"]    
    template_name = 'cadastros/contrato.html'
    success_url = reverse_lazy('index')

######################## UPDATE #######################

class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy("index")

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = [ 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy("index")

class ServicoUpdate(UpdateView):
    model = Servico
    fields = ['descricao_servico', 'valor']
    template_name ='cadastros/form.html'
    success_url = reverse_lazy('index')

class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['razao_social', 'cnpj', 'inscricao_estadual', 'endereco', 'minha_empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PropriedadeUpdate(UpdateView):
    model = Propriedade
    fields = ['nome_propriedade', 'endereco', 'area_propriedade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ['nome', 'endereço', 'cpf', 'rg', 'sexo', 'telefone', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ContratoUpdate(UpdateView):
    model = Contrato
    fields = ['servico', "propriedade", "data_inicial", "data_final", "registrado_por", "registrado_em", "contratante"]    
    template_name = 'cadastros/contrato.html'
    success_url = reverse_lazy('index')

######################## DELETE #######################
class EstadoDelete(DeleteView):
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')


class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class ServicoDelete(DeleteView):
    model = Servico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class EmpresaDelete(DeleteView):
    model = Empresa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class PropriedadeDelete(DeleteView):
    model = Propriedade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class PerfilDelete(DeleteView):
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

##########################listView#######################

class EstadoList(ListView):
    model = Estado
    template_name = 'cadastros/listar/estado.html'

class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listar/cidade.html'

class ServicoList(ListView):
    model = Servico
    template_name = 'cadastros/listar/servico.html'

class EmpresaList(ListView):
    model= Empresa
    template_name = 'cadastros/listar/empresa.html'

class PropriedadeList(ListView):
    model = Propriedade
    template_name = 'cadastros/listar/propriedade.html'

class PerfilList(ListView):
    model = Perfil
    template_name = 'cadastros/listar/perfis.html'
