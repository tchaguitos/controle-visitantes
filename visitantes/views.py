from django.shortcuts import render, redirect
from django.contrib import messages

from visitantes.models import Visitante
from visitantes.forms import VisitanteForm

from django.shortcuts import get_object_or_404

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
