# Generated by Django 5.1.3 on 2024-12-13 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('disponibilidade', models.BooleanField(default=True)),
                ('contratada', models.BooleanField(default=True)),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=10)),
                ('data_nascimento', models.DateField()),
                ('data_contratacao', models.DateTimeField()),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('genero', models.CharField(blank=True, choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], max_length=9, null=True)),
                ('salario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('turno', models.CharField(blank=True, choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite'), ('Flexível', 'Flexível')], max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Médico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('especializacao', models.CharField(choices=[('Clínica Geral', 'Clínica Geral'), ('Pediatria', 'Pediatria'), ('Ginecologia', 'Ginecologia'), ('Cardiologia', 'Cardiologia'), ('Ortopedia', 'Ortopedia')], max_length=50)),
                ('disponibilidade', models.BooleanField(default=True)),
                ('contratada', models.BooleanField(default=True)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('genero', models.CharField(blank=True, choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], max_length=9, null=True)),
                ('salario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('turno', models.CharField(blank=True, choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite'), ('Flexível', 'Flexível')], max_length=8, null=True)),
                ('data_contratacao', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Remédio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('laboratorio', models.CharField(max_length=150)),
                ('bula', models.TextField()),
                ('tipo', models.CharField(choices=[('Analgésico', 'Analgésico'), ('Antibiótico', 'Antibiótico'), ('Corticóide', 'Corticóide'), ('Descongestionante', 'Descongestionante')], max_length=17)),
                ('quantidade_estoque', models.PositiveIntegerField(default=0)),
                ('data_validade', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sintoma', models.CharField(max_length=300)),
                ('situacao', models.CharField(choices=[('Estável', 'Estável'), ('Moderado', 'Moderado'), ('Grave', 'Grave'), ('Crítico', 'Crítico')], default='Estável', max_length=12)),
                ('estado_consulta', models.CharField(choices=[('Triagem', 'Triagem'), ('Em Consulta', 'Em Consulta'), ('Alta', 'Alta')], default='Triagem', max_length=12)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=10)),
                ('telefone_familiar', models.CharField(max_length=10)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('cpf',), name='unique_paciente_cpf')],
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estagio_consulta', models.CharField(choices=[('Agendada', 'Agendada'), ('Concluída', 'Concluída')], default='agendada', max_length=12)),
                ('sintoma', models.CharField(max_length=100)),
                ('data_consulta', models.DateTimeField()),
                ('id_enfermeiro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.enfermeiro')),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.médico')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.paciente')),
                ('id_medicação', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app1.remédio')),
            ],
        ),
    ]
