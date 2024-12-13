from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
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
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outro', 'Outro'),
    ]

    ESPECIALIZACAO = [
        ('Clínica Geral', 'Clínica Geral'),
        ('Pediatria', 'Pediatria'),
        ('Ginecologia', 'Ginecologia'),
        ('Cardiologia', 'Cardiologia'),
        ('Ortopedia', 'Ortopedia'),
    ]

    TURNO = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
        ('Flexível', 'Flexível'),
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
    genero = models.CharField(max_length=9, choices=GENERO, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    turno = models.CharField(max_length=8, choices=TURNO, blank=True, null=True)
    data_contratacao = models.DateTimeField(blank=False)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Enfermeiro(models.Model):
    TURNO = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
        ('Flexível', 'Flexível'),
    ]

    GENERO = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outro', 'Outro'),
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
    genero = models.CharField(max_length=9, choices=GENERO, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    turno = models.CharField(max_length=8, choices=TURNO, blank=True, null=True)
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
    estagio_consulta = models.CharField(max_length=12, choices=[('Agendada', 'Agendada'), ('Concluída', 'Concluída')], default='agendada')
    
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    id_enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.PROTECT)
    id_medico = models.ForeignKey(Médico, on_delete=models.PROTECT)
    id_medicação = models.ForeignKey(Remédio, on_delete=models.PROTECT, blank=True, null=True)
    sintoma = models.CharField(max_length=100, blank=False)
    data_consulta = models.DateTimeField()
    observacao = models.TextField(blank=True)
    diagnostico = models.TextField()

    def __str__(self):
        return f"Consulta de {self.id_paciente} com {self.id_medico} em {self.data_consulta.strftime('%d/%m/%Y às %H:%M')}"


    