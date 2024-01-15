
from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views

from apps.api import urls as api_urls
from apps.dashboard import views as dashboard_views
from apps.visitantes import views as visitantes_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/", include('rest_framework.urls')),
    path(
        "api/",
        include(api_urls),
        name="api"
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="logout.html"
        ),
        name="logout"
    ),

    path(
        "",
        dashboard_views.index,
        name="index",
    ),

    path(
        "registrar-vistante/",
        visitantes_views.registrar_visitante,
        name="registrar_visitante",
    ),

    path(
        "visitantes/<uuid:token>/",
        visitantes_views.informacoes_visitante,
        name="informacoes_visitante",
    ),

    path(
        "visitantes/<uuid:token>/finalizar-visita/",
        visitantes_views.finalizar_visita,
        name="finalizar_visita"
    )
]
