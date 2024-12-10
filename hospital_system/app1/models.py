from django.db import models
from django.db.models import UniqueConstraint

class Paciente(models.Model):
    class Situacao(models.TextChoices):
        ESTAVEL = 'Estável', 'Estável'
        PRIORITARIO = 'Prioritário', 'Prioritário'
        EMERGENCIA = 'Emergência', 'Emergência'

    nome = models.CharField(max_length=100, blank=False)
    sintoma = models.CharField(max_length=300, blank=False)
    situacao = models.CharField(max_length=12, choices=Situacao.choices, default=Situacao.ESTAVEL, blank=False)
    cpf = models.CharField(max_length=14, blank=False)
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max_length=10, blank=False)
    telefone_familiar = models.CharField(max_length=10, blank=False)


    class Meta:
        constraints = [
            UniqueConstraint(fields=['cpf'], name='unique_paciente_cpf')  # Um nome único por paciente.
        ]

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

class Médico(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    especializacao = models.CharField(max_length=100, blank=100)
    disponibilidade = models.BooleanField()
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max_length=10, blank = False)

    def __str__(self):
        return self.nome

class Enfermeira(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    disponibilidade = models.BooleanField()
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max_length=10, blank = False)
    
    def __str__(self):
        return self.nome

class Remédio(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    laboratorio = models.CharField(max_length=150, blank=False)
    bula = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete = models.PROTECT)
    doença = models.CharField(max_length=100, blank=False)
    id_enfermeira = models.ForeignKey(Enfermeira, on_delete = models.PROTECT)
    id_medico = models.ForeignKey(Médico, on_delete = models.PROTECT)
    id_medicação = models.ForeignKey(Remédio, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.id_paciente, self.id_enfermeira, self.id_medico, self.id_medicação
    