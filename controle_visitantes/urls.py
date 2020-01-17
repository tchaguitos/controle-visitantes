from django.contrib import admin
from django.urls import path

import usuarios.views
import visitantes.views

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        usuarios.views.index,
        name="index",
    ),

    path(
        "registrar-vistante/",
        visitantes.views.registrar_visitante,
        name="registrar_visitante",
    ),

    path(
        "visitantes/<slug:token>/",
        visitantes.views.informacoes_visitante,
        name="informacoes_visitante",
    ),
]
