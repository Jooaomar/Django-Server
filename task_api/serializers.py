from rest_framework import serializers
from .models import Task


CHOICE_SITUACAO =  [('nova','nova'),
                    ('em andamento','em andamento'),
                    ('pendente', 'pendente'),
                    ('resolvida','resolvida'),
                    ('cancelada','cancelada')]

class TasksSerializer(serializers.ModelSerializer):

    descricao = serializers.CharField()
    situacao = serializers.ChoiceField(choices=CHOICE_SITUACAO)
    responsavel = serializers.CharField(max_length=250, default='')

    def validate_descricao(self, value):
        return value.capitalize()
    
    def validate_situacao(self, value):
        return value.capitalize()
    
    def validate_responsavel(self, value):
        return value.capitalize()

    class Meta:
        
        model = Task
        fields = '__all__'