from django.shortcuts import render
from visitantes.models import Visitante


def index(request):

    visitantes = Visitante.objects.all()

    visitantes_em_visita = visitantes.filter(
        status="EM_VISITA"
    ).count()

    visitantes_aguardando = visitantes.filter(
        status="AGUARDANDO"
    ).count()

    context = {
        "nome_pagina": "Página inicial",
        "visitantes": visitantes,
        "visitantes_em_visita": visitantes_em_visita,
        "visitantes_aguardando": visitantes_aguardando,
    }

    return render(request, "index.html", context)
