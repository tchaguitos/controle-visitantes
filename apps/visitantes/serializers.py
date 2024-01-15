from rest_framework import serializers

from visitantes.models import Visitante

class VisitanteSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(source="get_cpf")
    registrado_por = serializers.StringRelatedField(many=False)

    class Meta:
        model = Visitante
        fields = [
            "token", "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "status", "horario_chegada", "horario_autorizacao",
            "horario_saida", "placa_veiculo", "morador_responsavel", "registrado_por"
        ]
