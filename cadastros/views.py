from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.detail import DetailView

from .models import *

from django.views.generic.list import ListView

from django.urls import reverse_lazy


class EstadoCreate(LoginRequiredMixin, CreateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Cadastro de Estado"
            context['botao'] = "Cadastrar"
            context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

            return context


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')


def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Cadastro de Cidade"
            context['botao'] = "Cadastrar"
            context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

            return context


class ServicoCreate(LoginRequiredMixin, CreateView):
    model = Servico
    fields = ['descricao_servico', 'valor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servico')

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Cadastro de Serviço"
            context['botao'] = "Cadastrar"
            context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

            return context


class EmpresaCreate(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = ['nome_proprietario', 'cpf', 'rg', 'razao_social', 'cnpj',
        'inscricao_estadual', 'endereco', 'minha_empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-empresa')

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Cadastro de Empresa"
            context['botao'] = "Cadastrar"

            return context


class PropriedadeCreate(LoginRequiredMixin, CreateView):
    model = Propriedade
    fields = ['nome_propriedade', 'endereco', 'area_propriedade', 'cidade', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-propriedade')

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Cadastro de Propriedade"
            context['botao'] = "Cadastrar"
            context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
            return context

class ContratoCreate(LoginRequiredMixin, CreateView):
    model = Contrato
    fields = ["cidade", "servico", "propriedade", "registrado_por", "data_inicial", 
                "data_final", "contratante", "contratada"]    
    template_name = 'cadastros/contrato.html'
    success_url = reverse_lazy('listar-contrato')

    def form_valid(self, form):

        # Define o usuário como usuário logado
        form.instance.registrado_por = self.request.user
        
        url = super().form_valid(form)

        return url
        
class ConfiguracaoSistemaCreate(LoginRequiredMixin, CreateView):
    model = ConfiguracaoSistema
    fields = ['razao_social', 'nome_fantasia', 'cnpj',
        'inscricao_estadual', 'cidade', 'endereco', 'bairro', 'cep', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)

            context['titulo'] = "Configuração sistema"
            context['botao'] = "Cadastrar"

            return context

######################## UPDATE #######################

class EstadoUpdate(LoginRequiredMixin, UpdateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy("listar-estado")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Estados"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy("listar-cidade")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Cidades"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

class ServicoUpdate(LoginRequiredMixin, UpdateView):
    model = Servico
    fields = ['descricao_servico', 'valor']
    template_name ='cadastros/form.html'
    success_url = reverse_lazy('listar-servico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Servicos"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

class EmpresaUpdate(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = ['nome_proprietario', 'cpf', 'rg', 'razao_social', 'cnpj', 'inscricao_estadual', 'endereco', 'minha_empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-empresa')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Empresas"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

class PropriedadeUpdate(LoginRequiredMixin, UpdateView):
    model = Propriedade
    fields =['nome_propriedade', 'endereco', 'area_propriedade', 'cidade', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-propriedade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Propriedades"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    login_url =reverse_lazy('login')
    model = Perfil
    fields = ['nome', 'endereço', 'cpf', 'rg', 'sexo', 'telefone', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-perfil')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de perfil"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

class ContratoUpdate(LoginRequiredMixin, UpdateView):
    model = Contrato
    fields = ['servico', "propriedade", "data_inicial", "data_final", "contratante"]    
    template_name = 'cadastros/contrato.html'
    success_url = reverse_lazy('listar-contrato')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de contrato"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

######################## DELETE #######################
class EstadoDelete(LoginRequiredMixin, DeleteView):
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')


class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')

class ServicoDelete(LoginRequiredMixin, DeleteView):
    model = Servico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servico')

class EmpresaDelete(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-empresa')

class PropriedadeDelete(LoginRequiredMixin, DeleteView):
    model = Propriedade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-propriedade')

##########################listView#######################

class EstadoList(LoginRequiredMixin, ListView):
    model = Estado
    template_name = 'cadastros/listar/estado.html'

class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = 'cadastros/listar/cidade.html'

class ServicoList(LoginRequiredMixin, ListView):
    model = Servico
    template_name = 'cadastros/listar/servico.html'

class EmpresaList(LoginRequiredMixin, ListView):
    model= Empresa
    template_name = 'cadastros/listar/empresa.html'

class PropriedadeList(LoginRequiredMixin, ListView):
    model = Propriedade
    template_name = 'cadastros/listar/propriedade.html'

class ContratoList(LoginRequiredMixin, ListView):
    model = Contrato
    template_name = 'cadastros/listar/contrato_list.html'


###################DetailView#########################

class ContratoDetailView(LoginRequiredMixin, DetailView):
    model = Contrato
    template_name = 'cadastros/detalhe/contrato.html' # Arrumei aqui para o arquivo certo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
