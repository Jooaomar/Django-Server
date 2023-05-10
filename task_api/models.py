from django.db import models

CHOICE_NIVEL = [('1', '1'),
                ('3','3'),
                ('5','5'),
                ('8','8')]

CHOICE_SITUACAO =  [('NOVA','NOVA'),
                    ('EM ANDAMENTO','EM ANDAMENTO'),
                    ('PENDENTE', 'PENDENTE'),
                    ('RESOLVIDA','RESOLVIDA'),
                    ('CANCELADO','CANCELADO')]

CHOICE_PRIORIDADE = [('1', '1'),
                     ('2','2'),
                     ('3','3')]

class Task(models.Model):

    responsavel = models.CharField(max_length=250, blank=True, default='')
    descricao = models.TextField()
    nivel = models.IntegerField(max_length=1, choices=CHOICE_NIVEL)
    situacao = models.CharField(max_length=12,choices=CHOICE_SITUACAO)
    prioridade = models.IntegerField(max_length=1, choices=CHOICE_PRIORIDADE)
