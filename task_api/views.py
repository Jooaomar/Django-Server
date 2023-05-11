from rest_framework.views import APIView, Response,status
from django.http import Http404
from rest_framework import generics

from .models import Task
from .serializers import TasksSerializer

class ListarCriarTask(APIView):

    def get(self, request):
        serializer = TasksSerializer(Task.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalheAtualizarRemoverTask(APIView):

    def get_filme(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        filme = self.get_filme(pk)
        serializer = TasksSerializer(filme)
        return Response(serializer.data)

    def put(self, request, pk):
        filme = self.get_filme(pk)
        serializer = TasksSerializer(filme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        filme = self.get_filme(pk)
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListSituacaoNivelPrioridade(generics.ListAPIView):
    serializer_class = TasksSerializer
    
    def get_queryset(self):
        queryset = Task.objects.all()
        nivel = self.request.query_params.get('nivel')
        situacao = self.request.query_params.get('situacao')
        prioridade = self.request.query_params.get('prioridade')
        if nivel:
            queryset = queryset.filter(nivel=nivel)
        if situacao:
            queryset = queryset.filter(situacao=situacao)
        if prioridade:
            queryset = queryset.filter(prioridade=prioridade)
        return queryset
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "Nenhum resultado encontrado."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

