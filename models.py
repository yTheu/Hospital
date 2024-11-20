from django.db import models

class Paciente(models.Model):
    class Situacao(models.TextChoices):
        LEVE = 'leve', 'leve'
        ESTAVEL = 'estavel', 'estavel'
        GRAVE = 'grave', 'grave'

    nome = models.CharField(max_length=100, blank=False)
    sintoma = models.CharField(max_length=10, blank=False)
    situacao = models.CharField(max_length=10, choices=Situacao.choices, default=Situacao.leve, blank=False)
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
    especializacao = models.CharField(max_length=100, blank=100)
    disponibilidade = models.BooleanField(bool)
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max=10, blank = False)

class Secretaria(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    disponibilidade = models.BooleanField(bool)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max=10, blank = False)

class Remedio(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    laboratorio = models.CharField(max_length=150, blank=False)
    bula = models.CharField(max_length=300, blank=False)

class Consulta(models.Model):
    id_paciente = models.ForeignKey(Paciente,models.PROTECT)
    doença = models.CharField(max_length=100, blank=False)
    id_secretaria = models.ForeignKey(Secretaria,models.PROTECT)
    id_medico = models.ForeignKey(Medico,models.PROTECT)
    id_medicação = models.ForeignKey(Remedio,models.PROTECT)


