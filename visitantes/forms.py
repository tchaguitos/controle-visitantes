from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]
        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante é obrigatório para cadastro",
            },
            "cpf": {
                "required": "O CPF do visitante é obrigatório para cadastro"
            },
            "data_nascimento": {
                "required": "A data de nascimento do visitante é obrigatória para cadastro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "Por favor, informe o número da casa a ser visitada"
            },
        }


class AutorizaVisitanteForm(forms.ModelForm):
    autorizado_por = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = [
            "autorizado_por",
        ]
