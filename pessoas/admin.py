from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "conhecidoPor", "cpf", "dataNascimento",
                    "sexo", "estadoCivil", "escolaridade", "nacionalidade")
    search_fields = ("nome", "cpf")
    list_filter = ("sexo", "estadoCivil", "escolaridade",)
