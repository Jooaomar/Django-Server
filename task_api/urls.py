from django.urls import path
# from .views import ListarCriarTask, DetalheAtualizarRemoverTask, ListSituacaoNivelPrioridade
from task_api import views

# urlpatterns = [
#     path('tarefas/', ListarCriarTask.as_view(), name= 'listar-criar-tarefa'),
#     path('tarefas/<int:pk>', DetalheAtualizarRemoverTask.as_view(), name='detalhar-atualizar-remover'),
#     path('search/', ListSituacaoNivelPrioridade.as_view(), name='Situação-Nivel-Prioridade'),
# ]

urlpatterns = [
    path('task_api/', views.task_list),
    path('task_api/<int:pk>/', views.task_detail),
]