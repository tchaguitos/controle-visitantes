from django.shortcuts import render

def registrar_visitante(request):
    return render(request, "registrar_visitante.html", {})

