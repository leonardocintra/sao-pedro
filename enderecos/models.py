from django.db import models

from pessoas.models import Pessoa


class Endereco(models.Model):
    pessoa = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, related_name="enderecos")

    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=8)
    pais = models.CharField(max_length=50, default="Brasil")

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"
