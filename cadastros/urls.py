from django.urls import path 

from .views import EstadoCreate, CidadeCreate, EmpresaCreate, PropriedadeCreate, ServicoCreate
from .views import EmpresaUpdate, PropriedadeUpdate, ServicoUpdate
from .views import EstadoList, CidadeList, EmpresaList, PropriedadeList, ServicoList
from .views import EstadoDelete, CidadeDelete, EmpresaDelete, PropriedadeDelete, ServicoDelete

urlpatterns = [
    #path('cadastros/Estado', EstadoCreate.as_view(), name = "cadastro-Estado")
    #path('cadastros/cidade', CidadeCreate.as_view(), name ="cadastro-cidade"),           
    path('cadastros/empresa/', EmpresaCreate.as_view(), name ="cadastro-empresa"),
    path('cadastros/propriedade/', PropriedadeCreate.as_view(), name ="cadastro-propriedade"),
    path('cadastros/servico/', ServicoCreate.as_view(), name ="cadastro-servico"),

    path('editar/empresa/<int:pk>', EmpresaUpdate.as_view(), name ='editar-empresa'),    
    path('editar/propriedade/<int:pk>', PropriedadeUpdate.as_view(), name ='editar-propriedade'),
    path('editar/servico/<int:pk>', ServicoUpdate.as_view(), name ='editar-servico'),

    path('excluir/estado/<int:pk>', EstadoDelete.as_view(), name='excluir-estado'),
    path('excluir/cidade/<int:pk>', CidadeDelete.as_view(), name='excluir-cidade'),
    path('excluir/propriedade/<int:pk>', PropriedadeDelete.as_view(), name='excluir-propriedade'),
    path('excluir/Empresa/<int:pk>', EmpresaDeleteDelete.as_view(), name='excluir-empresa'),
    path('excluir/servico/<int:pk>', servicoDelete.as_view(), name='excluir-servico'),


    path('listar/estado/', EstadoList.as_view(), name='listrar-estado'),
    path('listar/cidade/', CidadeList.as_view(), name='listrar-cidade'),
    path('listar/empresa/', EmpresaList.as_view(), name='listrar-empresa'),
    path('listar/propriedade/', PropriedadeList.as_view(), name='listrar-propriedade'),
    path('listar/servico/', ServicoList.as_view(), name='listrar-servico'),

   
]