from django.contrib import admin

from .models import Estado, Cidade, User, Perfil, Servico, Empresa, Propriedade, Contrato
# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(User)
admin.site.register(Perfil)
admin.site.register(Servico)
admin.site.register(Empresa)
admin.site.register(Propriedade)
admin.site.register(Contrato)



