from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        "usuario_logado": request.user
    }

    return render(request, "index.html", context)
