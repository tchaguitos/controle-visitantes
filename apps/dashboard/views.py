from django.shortcuts import render
from visitantes.models import Visitante

from datetime import datetime


def index(request):

    visitantes = Visitante.objects.all().order_by("-horario_chegada")

    hora_atual = datetime.now()
    mes_atual = hora_atual.month

    visitantes_em_visita = visitantes.filter(
        status="EM_VISITA"
    ).count()

    visitantes_aguardando = visitantes.filter(
        status="AGUARDANDO"
    ).count()

    visitantes_finalizado = visitantes.filter(
        status="FINALIZADO"
    ).count()

    visitantes_mes = visitantes.filter(
        horario_chegada__month=mes_atual
    ).count()

    context = {
        "nome_pagina": "Página inicial",
        "visitantes": visitantes,
        "visitantes_em_visita": visitantes_em_visita,
        "visitantes_aguardando": visitantes_aguardando,
        "visitantes_finalizado": visitantes_finalizado,
        "visitantes_mes": visitantes_mes
    }

    return render(request, "index.html", context)
