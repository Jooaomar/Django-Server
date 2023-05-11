from django.db import models

CHOICE_NIVEL = [(1, 1),
                (3,3),
                (5,5),
                (8,8)]


CHOICE_PRIORIDADE = [(1, 1),
                     (2,2),
                     (3,3)]

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200, blank=True, default='')
    responsavel = models.CharField(max_length=250, blank=True, default='')
    nivel = models.IntegerField(choices=CHOICE_NIVEL)
    situacao = models.CharField(max_length=12)
    prioridade = models.IntegerField(choices=CHOICE_PRIORIDADE)

    class Meta:
        ordering = ['created']
