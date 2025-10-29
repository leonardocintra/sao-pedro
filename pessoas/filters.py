import django_filters

from pessoas.models import Pessoa


class PessoaFilter(django_filters.FilterSet):
    class Meta:
        model = Pessoa
        fields = ["cpf", "uuid"]  # Adicione outros campos conforme necessário
