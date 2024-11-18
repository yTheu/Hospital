from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    sintoma = models.CharField(max_length=10, blank=False)
    #situacao = models.Choices ["leve": "Leve","estavel": "Estável","grave": "Grave"]
    cpf = models.CharField(max_length=11, blank=False)
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max=10, blank=False)
    telefone_familiar = models.CharField(max=10, blank=False)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

class Medico(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    especializacao = models.CharField(max_lenght=100, blank=100)
    disponibilidade = models.BooleanField(bool)
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max=10, blank = False)
