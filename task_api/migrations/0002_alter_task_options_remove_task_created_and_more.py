# Generated by Django 4.0.4 on 2023-05-10 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.AlterField(
            model_name='task',
            name='nivel',
            field=models.CharField(choices=[('1', '1'), ('3', '3'), ('5', '5'), ('8', '8')], max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='prioridade',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='resposavel',
            field=models.CharField(blank=True, default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='situacao',
            field=models.CharField(choices=[('NOVA', 'NOVA'), ('EM ANDAMENTO', 'EM ANDAMENTO'), ('PENDENTE', 'PENDENTE'), ('RESOLVIDA', 'RESOLVIDA'), ('CANCELADO', 'CANCELADO')], max_length=12),
        ),
    ]
