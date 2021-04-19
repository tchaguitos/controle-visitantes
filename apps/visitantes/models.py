from uuid import uuid4
from django.db import models


class Visitante(models.Model):

    STATUS_VISITANTE = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "Visita finalizada"),
    ]

    token = models.UUIDField(
        default=uuid4,
        editable=False,
        unique=True
    )

    nome_completo = models.CharField(
        verbose_name="Nome completo", max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False
    )

    numero_casa = models.CharField(
        verbose_name="Número da casa a ser visitada",
        max_length=3,
    )

    status = models.CharField(
        verbose_name="Status",
        max_length=22,
        choices=STATUS_VISITANTE,
        default="AGUARDANDO",
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na recepção", auto_now_add=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        null=True,
        blank=True,
        auto_now=False,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condomínio",
        null=True,
        blank=True,
        auto_now=False,
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.CASCADE
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do veículo",
        max_length=10,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
        null=True,
    )

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao

        return "Visitante aguardando autorização"

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel

        return "Visitante aguardando autorização"

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida

        return "Horário de saída não registrado"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo

        return "Veículo não registrado"

    def get_cpf(self):
        cpf = self.cpf

        cpf_mascarado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        return cpf_mascarado

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self):
        return self.nome_completo
