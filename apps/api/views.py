from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db import IntegrityError, InternalError

from visitantes.models import Visitante
from visitantes.serializers import VisitanteSerializer

class VisitanteAPI(viewsets.ViewSet):
    def get_queryset(self):
        return Visitante.objects.order_by(
            "-horario_chegada"
        )

    def list(self, request):
        queryset = self.get_queryset()
        serializer = VisitanteSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        visitante = get_object_or_404(queryset, token=pk)

        serializer = VisitanteSerializer(visitante)

        return Response(serializer.data)
