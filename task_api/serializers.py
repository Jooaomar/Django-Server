from rest_framework import serializers
from task_api.models import Task

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'created', 'resposavel', 'descricao', 'nivel', 'situacao', 'prioridade']