from django.urls import path

from .views import *
 
urlpatterns = [
    path('cadastros/empresa/', EmpresaCreate.as_view(), name ="cadastro-empresa"),
    path('cadastros/propriedade/', PropriedadeCreate.as_view(), name ="cadastro-propriedade"),
    path('cadastros/servico/', ServicoCreate.as_view(), name ="cadastro-servico"),

]