from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from visitantes.models import Visitante

from datetime import datetime


@login_required
def index(request):

    # buscando todos os visitantes e ordenando por dia e hora de chegada
    visitantes = Visitante.objects.order_by(
        "-horario_chegada"
    )

    # separando visitantes por status
    visitantes_em_visita = visitantes.filter(
        status="EM_VISITA"
    ).count()

    visitantes_aguardando = visitantes.filter(
        status="AGUARDANDO"
    ).count()

    visitantes_finalizado = visitantes.filter(
        status="FINALIZADO"
    ).count()

    # filtrando visitantes por data (mês atual)
    hora_atual = datetime.now()
    mes_atual = hora_atual.month

    visitantes_mes = visitantes.filter(
        horario_chegada__month=mes_atual
    ).count()

    # paginando resultados para exibir de 10 em 10 itens
    numero_pagina = request.GET.get('page', 1)
    visitantes_paginados = Paginator(visitantes, 10)
    pagina_obj = visitantes_paginados.get_page(numero_pagina)

    context = {
        "nome_pagina": "Página inicial",
        "visitantes_em_visita": visitantes_em_visita,
        "visitantes_aguardando": visitantes_aguardando,
        "visitantes_finalizado": visitantes_finalizado,
        "visitantes_mes": visitantes_mes,
        "pagina_obj": pagina_obj
    }

    return render(request, "index.html", context)
