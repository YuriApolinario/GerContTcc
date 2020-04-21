from django.db import models

# Create your models here.


class Estado(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    mome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + " - " + self.nome


class Cidade(models.Model):
    nome = models .CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + " - " + self.estado.sigla

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length= 20)


class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15, unique=True)
    inscricao_estadual = models.CharField(max_length=45)
    endereço = models.CharField(max_length=100)
    minha_empresa = models.CharField(max_length=100)

class Propriedade(models.Model):
    nome_propriedade = models.CharField(max_length=45)
    endereço = models.CharField(max_length=100)
    area_propriedade = models.CharField(max_length=45)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)


