import django_filters

from pessoas.models import Pessoa


class PessoaFilter(django_filters.FilterSet):
    class Meta:
        model = Pessoa
        # Adicione outros campos conforme necessário
        fields = ["cpf", "uuid", "sexo", "estadoCivil"]
