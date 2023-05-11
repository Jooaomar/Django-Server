from rest_framework.views import APIView, Response,status
from django.http import Http404
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Task
from .serializers import TasksSerializer

# class ListarCriarTask(APIView):

#     def get(self, request):
#         serializer = TasksSerializer(Task.objects.all(), many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TasksSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def task_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TasksSerializer(task, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# class DetalheAtualizarRemoverTask(APIView):

#     def get_filme(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         filme = self.get_filme(pk)
#         serializer = TasksSerializer(filme)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         filme = self.get_filme(pk)
#         serializer = TasksSerializer(filme, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         filme = self.get_filme(pk)
#         filme.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def task_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TasksSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)
    

# class ListSituacaoNivelPrioridade(generics.ListAPIView):
#     serializer_class = TasksSerializer
    
#     def get_queryset(self):
#         queryset = Task.objects.all()
#         nivel = self.request.query_params.get('nivel')
#         situacao = self.request.query_params.get('situacao')
#         prioridade = self.request.query_params.get('prioridade')
#         if nivel:
#             queryset = queryset.filter(nivel=nivel)
#         if situacao:
#             queryset = queryset.filter(situacao=situacao)
#         if prioridade:
#             queryset = queryset.filter(prioridade=prioridade)
#         return queryset
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         if not queryset.exists():
#             return Response({"detail": "Nenhum resultado encontrado."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

