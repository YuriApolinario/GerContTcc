from django.urls import path 

from .views import EstadoCreate, CidadeCreate, EmpresaCreate, PropriedadeCreate, ServicoCreate, PerfilCreate, ContratoCreate
from .views import EmpresaUpdate, PropriedadeUpdate, ServicoUpdate, PerfilUpdate
from .views import EstadoList, CidadeList, EmpresaList, PropriedadeList, ServicoList, PerfilList
from .views import EstadoDelete, CidadeDelete, EmpresaDelete, PropriedadeDelete, ServicoDelete, PerfilDelete

urlpatterns = [
    path('cadastros/contrato', ContratoCreate.as_view(), name = "cadastro-contrato"),
    path('cadastros/estado', EstadoCreate.as_view(), name = "cadastro-estado"),
    path('cadastros/cidade', CidadeCreate.as_view(), name = "cadastro-cidade"),           
    path('cadastros/empresa/', EmpresaCreate.as_view(), name ="cadastro-empresa"),
    path('cadastros/propriedade/', PropriedadeCreate.as_view(), name ="cadastro-propriedade"),
    path('cadastros/servico/', ServicoCreate.as_view(), name ="cadastro-servico"),
    path('cadastros/perfil/', PerfilCreate.as_view(), name ="cadastro-perfil"),


    path('editar/estado/<int:pk>', EstadoCreate.as_view(), name = "editar-estado"),
    path('cadastros/cidade/<int:pk>', CidadeCreate.as_view(), name ="editar-cidade"),
    path('editar/empresa/<int:pk>', EmpresaUpdate.as_view(), name ="editar-empresa"),    
    path('editar/propriedade/<int:pk>', PropriedadeUpdate.as_view(), name ="editar-propriedade"),
    path('editar/servico/<int:pk>', ServicoUpdate.as_view(), name ="editar-servico"),
    path('editar/perfil/<int:pk>', PerfilUpdate.as_view(), name ="editar-perfil"),


    path('excluir/estado/<int:pk>', EstadoDelete.as_view(), name="excluir-estado"),
    path('excluir/cidade/<int:pk>', CidadeDelete.as_view(), name="excluir-cidade"),
    path('excluir/propriedade/<int:pk>', PropriedadeDelete.as_view(), name="excluir-propriedade"),
    path('excluir/Empresa/<int:pk>', EmpresaDelete.as_view(), name="excluir-empresa"),
    path('excluir/servico/<int:pk>', ServicoDelete.as_view(), name="excluir-servico"),
    path('excluir/perfil/<int:pk>', PerfilDelete.as_view(), name ="excluir-perfil"),



    path('listar/estado/', EstadoList.as_view(), name="listar-estado"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidade"),
    path('listar/empresa/', EmpresaList.as_view(), name="listar-empresa"),
    path('listar/propriedade/', PropriedadeList.as_view(), name="listar-propriedade"),
    path('listar/servico/', ServicoList.as_view(), name="listar-servico"),
    path('listar/perfil/', PerfilList.as_view(), name ="listar-perfil"),


   
]