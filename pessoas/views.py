from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by("-id")
    serializer_class = PessoaSerializer
