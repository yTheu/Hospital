from django.db import models
from django.db.models import UniqueConstraint
from django.db import models

class Paciente(models.Model):
    class Situacao(models.TextChoices):
        ESTAVEL = 'Estável', 'Estável'
        MODERADO = 'Moderado', 'Moderado'
        GRAVE = 'Grave', 'Grave'
        CRÍTICO = 'Crítico', 'Crítico'

    class EstagioAtendimento(models.TextChoices):
        TRIAGEM = 'Triagem', 'Triagem'
        CONSULTA = 'Em Consulta', 'Em Consulta'
        ALTA = 'Alta', 'Alta'

    nome = models.CharField(max_length=100, blank=False)
    sintoma = models.CharField(max_length=300, blank=False)
    situacao = models.CharField(max_length=12, choices=Situacao.choices, default=Situacao.ESTAVEL, blank=False)
    estado_consulta = models.CharField(max_length=12, choices=EstagioAtendimento.choices, default=EstagioAtendimento.TRIAGEM, blank=False)
    cpf = models.CharField(max_length=14, blank=False)
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max_length=10, blank=False)
    telefone_familiar = models.CharField(max_length=10, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cpf'], name='unique_paciente_cpf')
        ]

    def __str__(self):
        return self.nome

class Médico(models.Model):
    GENERO = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro'),
    ]

    ESPECIALIZACAO = [
        ('CLINICA_GERAL', 'Clínica Geral'),
        ('PEDIATRIA', 'Pediatria'),
        ('GINECOLOGIA', 'Ginecologia'),
        ('CARDIOLOGIA', 'Cardiologia'),
        ('ORTOPEDIA', 'Ortopedia'),
    ]

    TURNO = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
        ('F', 'Flexível'),
    ]

    nome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    especializacao = models.CharField(max_length=50, choices=ESPECIALIZACAO, blank=False)
    disponibilidade = models.BooleanField(default=True)
    contratada = models.BooleanField(default=True)
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=150, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENERO, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    turno = models.CharField(max_length=1, choices=TURNO, blank=True, null=True)
    data_contratacao = models.DateTimeField(blank=False)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Enfermeiro(models.Model):
    TURNO = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
        ('F', 'Flexível'),
    ]

    GENERO = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    disponibilidade = models.BooleanField(default=True)
    contratada = models.BooleanField(default=True)
    endereco = models.CharField(max_length=250, blank=False)
    telefone = models.CharField(max_length=10, blank=False)
    data_nascimento = models.DateField(blank=False)
    data_contratacao = models.DateTimeField(blank=False)

    email = models.EmailField(max_length=150, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENERO, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    turno = models.CharField(max_length=1, choices=TURNO, blank=True, null=True)
    #foto = models.ImageField(upload_to='enfermeiros_fotos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"


class Remédio(models.Model):
    GENERO_CHOICES = [
        ('Analgésico', 'Analgésico'),
        ('Antibiótico', 'Antibiótico'),
        ('Corticóide', 'Corticóide'),
        ('Descongestionante', 'Descongestionante'),
    ]

    nome = models.CharField(max_length=100, blank=False)
    laboratorio = models.CharField(max_length=150, blank=False)
    bula = models.TextField(blank=False)
    tipo = models.CharField(max_length=17, choices=GENERO_CHOICES, blank=False)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    data_validade = models.DateField(blank=False)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    estagio_consulta = models.CharField(max_length=12, choices=[('agendada', 'Agendada'), ('concluída', 'Concluída')], default='agendada')
    
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    id_enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.PROTECT)
    id_medico = models.ForeignKey(Médico, on_delete=models.PROTECT)
    id_medicação = models.ForeignKey(Remédio, on_delete=models.PROTECT, blank=True, null=True)
    doença = models.CharField(max_length=100, blank=False)
    data_consulta = models.DateTimeField()
    
    def __str__(self):
        return f"Consulta de {self.id_paciente} com {self.id_medico} em {self.data_consulta.strftime('%d/%m/%Y às %H:%M')}"


    