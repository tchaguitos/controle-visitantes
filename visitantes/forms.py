from django import forms
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo", "autorizado_por",
        ]


class AutorizaVisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "status", "autorizado_por", "horario_autorizacao"
        ]
