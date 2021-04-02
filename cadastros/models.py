from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=50, verbose_name="nome do estado")

    def __str__(self):
        return "{} ({})".format(self.sigla, self.nome)

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
   

    def __str__(self):
        return self.nome + '/' + self.estado.sigla


class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length= 20)
    usuario = models.ForeignKey(User, on_delete= models.PROTECT, verbose_name="usuário")

    def __str__(self):
        return"{}({})".format(self.nome, self.endereco, self.cpf, self.sexo, self.telefone)


class Servico(models.Model):
    descricao_servico = models.CharField(max_length=100 )
    valor = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Valor R$")

    def  __str__(self):
            return "{} ({})".format(self.descricao_servico, self.valor)

class Empresa(models.Model):
    nome_proprietario = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=15)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    inscricao_estadual = models.CharField(max_length=45, verbose_name="Inscrição Estadual")
    endereco = models.CharField(max_length=100)
    minha_empresa = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({})".format(self.nome_proprietario, self.cpf, self.cnpj, self.razao_social, self.cnpj, self.inscricao_estadual, self.endereco, self.minha_empresa)

class Propriedade(models.Model):
    nome_propriedade = models.CharField(max_length=45)
    endereco = models.CharField(max_length=100)
    area_propriedade = models.CharField(max_length=45)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete= models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome_propriedade, self.endereco, self.area_propriedade, self.cidade, self.empresa)


class ConfiguracaoSistema(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    inscricao_estadual = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    email = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({})".format(self.razao_social, self.nome_fantasia, self.cnpj, self.inscricao_estadual, self.cidade,
        self.endereco, self.bairro, self.cep, self.email)

class Contrato(models.Model):
    servico = models.ForeignKey(Servico, on_delete= models.PROTECT)
    propriedade = models.ForeignKey(Propriedade, on_delete= models.PROTECT)
    data_inicial = models.DateField(default=date.today)
    data_final = models.DateField(default=date.today)
    registrado_por = models.ForeignKey(User, on_delete= models.PROTECT)
    registrado_em = models.DateField(auto_now=True)
    contratante = models.ForeignKey(Empresa, on_delete= models.PROTECT)
    contratada = models.ForeignKey(ConfiguracaoSistema, on_delete= models.PROTECT)
    cidade = models.ForeignKey(Cidade, on_delete= models.PROTECT)
    
