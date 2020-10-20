from django.db import models

# Create your models here.


class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=50, verbose_name="nome do estado")

    def __str__(self):
        return "{} ({})".format(self.sigla, self.nome)

class Cidade(models.Model):
    nome = models .CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.estado.nome)

class User(models.Model):
    usuario = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length= 20)
    user = models.ForeignKey(User, on_delete= models.PROTECT)

    def __str__(self):
        return"{}({})".format(self.nome, self.endereco, self.cpf, self.sexo, self.telefone)
class Servico(models.Model):
    descricao_servico = models.CharField(max_length=100)
    valor = models.FloatField(max_length=10)

    def  __str__(self):
            return "{} ({})".format(self.descricao_servico, self.valor)

class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15, unique=True)
    inscricao_estadual = models.CharField(max_length=45)
    endereco = models.CharField(max_length=100)
    minha_empresa = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({})".format(self.razao_social, self.cnpj, self.inscricao_estadual, self.endereco, self.minha_empresa)

class Propriedade(models.Model):
    nome_propriedade = models.CharField(max_length=45)
    endereco = models.CharField(max_length=100)
    area_propriedade = models.CharField(max_length=45)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome_propriedade, self.endereco, self.area_propriedade, self.cidade)

class Contrato(models.Model):
    servico = models.ForeignKey(Servico, on_delete= models.PROTECT)
    propriedade = models.ForeignKey(Propriedade, on_delete= models.PROTECT)
    data_inicial = models.DateField(max_length= 8)
    data_final = models.DateField(max_length= 8)
    registrado_por = models.ForeignKey(User, on_delete= models.PROTECT)
    registrado_em = models.DateField(max_length=8)
 
    contratada = models.ForeignKey(Empresa, on_delete= models.PROTECT)
    contratante = models.ForeignKey(Empresa, on_delete= models.PROTECT)

