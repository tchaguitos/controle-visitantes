import django_filters

from visitantes.models import Visitante


class VisitanteFilter(django_filters.FilterSet):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "numero_casa", "status"
        ]