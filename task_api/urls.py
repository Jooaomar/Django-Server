from django.urls import path
from .views import ListarCriarTask, DetalheAtualizarRemoverTask

urlpatterns = [
    path('tarefas/', ListarCriarTask.as_view(), name= 'listar-criar-tarefa'),
    path('tarefas/<int:pk>', DetalheAtualizarRemoverTask.as_view(), name='detalhar-atualizar-remover'),
]