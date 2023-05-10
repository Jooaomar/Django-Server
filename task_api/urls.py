from django.urls import path
from .views import ListarCriarTask, DetalheAtualizarRemoverTask, ListStituacaoNivelPrioridade

urlpatterns = [
    path('tarefas/', ListarCriarTask.as_view(), name= 'listar-criar-tarefa'),
    path('tarefas/<int:pk>', DetalheAtualizarRemoverTask.as_view(), name='detalhar-atualizar-remover'),
    path('tarefas/search/', ListStituacaoNivelPrioridade.as_view(), name='Situação-Nivel-Prioridade'),
]