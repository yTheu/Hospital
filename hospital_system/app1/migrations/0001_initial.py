# Generated by Django 5.1.3 on 2024-11-22 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Médico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('especializacao', models.CharField(blank=100, max_length=100)),
                ('disponibilidade', models.BooleanField()),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sintoma', models.CharField(max_length=10)),
                ('situacao', models.CharField(choices=[('leve', 'leve'), ('estavel', 'estavel'), ('grave', 'grave')], default='leve', max_length=10)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=10)),
                ('telefone_familiar', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Remédio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('laboratorio', models.CharField(max_length=150)),
                ('bula', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Secretária',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('disponibilidade', models.BooleanField()),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doença', models.CharField(max_length=100)),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.médico')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.paciente')),
                ('id_medicação', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.remédio')),
                ('id_secretaria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.secretária')),
            ],
        ),
    ]