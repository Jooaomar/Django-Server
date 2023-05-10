from django.db import models


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    resposavel = models.CharField(max_length=100, blank=True, default='')
    descricao = models.TextField()
    nivel = models.CharField(max_length=100, blank=True, default='')
    situacao = models.CharField(max_length=100, blank=True, default='')
    prioridade = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']