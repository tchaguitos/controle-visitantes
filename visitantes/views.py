from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest

from visitantes.models import Visitante

from visitantes.forms import VisitanteForm, AutorizaVisitanteForm

from django.shortcuts import get_object_or_404

from datetime import datetime

def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.registrado_por = request.user.porteiro

            visitante.save()

            messages.success(
                request,
                "Visitante registrado com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Registrar visitante",
        "form": form,
    }

    return render(request, "registrar_visitante.html", context)


def informacoes_visitante(request, token):

    visitante = get_object_or_404(Visitante, token=token)

    context = {
        "nome_pagina": "Informações de visitante",
        "visitante": visitante,
    }

    return render(request, "informacoes_visitante.html", context)


def autorizar_visitante(request, token):

    if request.method == "POST":
        visitante = get_object_or_404(Visitante, token=token)

        form = AutorizaVisitanteForm(request.POST, instance=visitante)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = datetime.now()

            visitante.save()

            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso"
            )

            return redirect("index")

        else:
            return HttpResponseBadRequest(form.errors.as_text())

    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )


def finalizar_visita(request, token):

    if request.method == "POST":
        visitante = get_object_or_404(Visitante, token=token)

        visitante.status = "FINALIZADO"
        visitante.horario_saida = datetime.now()

        visitante.save()

        messages.success(
            request,
            "Visita finalizada com sucesso"
        )

        return redirect("index")

    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )
