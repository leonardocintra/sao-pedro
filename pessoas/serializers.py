from rest_framework import serializers

from enderecos.serializers import EnderecoSerializer
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True)

    class Meta:
        model = Pessoa
        fields = [
            "id",
            "nome",
            "conhecidoPor",
            "cpf",
            "data_nascimento",
            "sexo",
            "estado_civil",
            "escolaridade",
            "nacionalidade",
            "foto",
            "enderecos",
        ]

    def validate_cpf(self, value):
        """
        Garante que o CPF seja único apenas se preenchido.
        """
        if value:
            qs = Pessoa.objects.filter(cpf=value)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError(
                    "Este CPF já está cadastrado.")
        return value
