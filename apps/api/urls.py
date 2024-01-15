from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import VisitanteAPI

router = DefaultRouter()

router.register(
    "visitantes",
    VisitanteAPI,
    basename="Visitante"
)

urlpatterns = [
    path("", include(router.urls)),
]
