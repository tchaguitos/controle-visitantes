from uuid import UUID
from typing import Optional
from http import HTTPMethod
from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from visitantes.models import Visitante
from visitantes.serializers import (
    VisitanteSerializer,
    CriarVisitanteSerializer,
    AutorizaVisitanteSerializer,
)

class VisitanteAPI(viewsets.ViewSet):
    def get_queryset(self):
        return Visitante.objects.order_by(
            "-horario_chegada"
        )

    def list(self, request):
        queryset = self.get_queryset()
        serializer = VisitanteSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk: Optional[UUID] = None):
        queryset = self.get_queryset()
        visitante = get_object_or_404(queryset, token=pk)

        serializer = VisitanteSerializer(visitante)

        return Response(serializer.data)

    def create(self, request):
        serializer = CriarVisitanteSerializer(data=request.data)

        if serializer.is_valid():
            visitante = serializer.save(registrado_por=request.user.porteiro)

            return Response(
                {"token": visitante.token},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=[HTTPMethod.PATCH], url_path="autoriza-entrada")
    def autoriza_entrada(self, request, pk: Optional[UUID] = None):
        queryset = self.get_queryset()
        visitante = get_object_or_404(queryset, token=pk)

        serializer = AutorizaVisitanteSerializer(
            instance=visitante,
            data=request.data
        )

        if serializer.is_valid():
            visitante = serializer.save(
                status="EM_VISITA",
                horario_autorizacao=datetime.utcnow(),
            )

            return Response(
                {"token": visitante.token},
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
