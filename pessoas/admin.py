from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "conhecidoPor", "cpf", "data_nascimento",
                    "sexo", "estado_civil", "escolaridade", "nacionalidade")
    search_fields = ("nome", "cpf")
    list_filter = ("sexo", "estado_civil", "escolaridade",)
