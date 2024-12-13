from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from app1.models import Médico, Enfermeiro, Paciente, Remédio, Consulta
from app1.forms import PacienteForm, ConsultaForm, MedicoForm, EnfermeiroForm, RemedioForm
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from datetime import datetime

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'adm/home.html')

def check_login_medico(func):
    def wrapper(request, *args, **kwargs):
        if 'medico_cpf' not in request.session:
            return redirect('medicos/login_medico')
        return func(request, *args, **kwargs)
    return wrapper

def login_medico(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        
        try:
            
            medico = Médico.objects.get(cpf=cpf)
            request.session['medico_id'] = medico.id
            messages.success(request, f'Bem-vindo, Dr(a). {medico.nome}!')
            return redirect('agenda_medica')

        except Médico.DoesNotExist:
            messages.error(request, 'CPF inválido ou não cadastrado.')
            return redirect('login_medico')

    return render(request, 'medico/login_medico.html')

@check_login_medico
def agenda_medica(request):
    medico_id = request.session.get('medico_id')

    if medico_id:
        try:
            medico = Médico.objects.get(id=medico_id)
            hoje = datetime.now()

            consultas_futuras = Consulta.objects.filter(id_medico=medico, data_consulta__gte=hoje)
            consultas_passadas = Consulta.objects.filter(id_medico=medico, data_consulta__lt=hoje)

            return render(request, 'medico/consultas/agenda_medica.html', {
                'medico': medico,
                'consultas_futuras': consultas_futuras,
                'consultas_passadas': consultas_passadas
            })

        except Médico.DoesNotExist:
            messages.error(request, 'Erro ao recuperar os dados do médico.')
            return redirect('login_medico')
    else:
        messages.error(request, 'Faça login para acessar esta página.')
        return redirect('login_medico')

@check_login_medico
def detalhar_consulta_medico(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    
    return render(request, 'medico/consultas/detalhar_consulta_medico.html', {'consulta': consulta})


def editar_consulta_medico(request, id):
    consulta = get_object_or_404(Consulta, id=id)

    if request.method == 'POST':
        # Atualizando os campos que podem ser editados
        diagnostico = request.POST.get('diagnostico')
        observacao = request.POST.get('observacao')
        medicamento_id = request.POST.get('medicamento')

        # Salvando as atualizações
        consulta.diagnostico = diagnostico
        consulta.observacao = observacao
        if medicamento_id:
            consulta.id_medicação = Remédio.objects.get(id=medicamento_id)
        
        consulta.save()
        messages.success(request, 'Consulta atualizada com sucesso!')
        return redirect('agenda_medica')

    remedios = Remédio.objects.all()  # Carregando todos os remédios para o select

    return render(request, 'medico/consultas/editar_consulta_medico.html', {
        'consulta': consulta,
        'remedios': remedios
    })


def login_paciente(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')

        try:
            paciente = Paciente.objects.get(cpf=cpf)
            
            request.session['paciente_cpf'] = cpf
            messages.success(request, f'Bem-vindo, {paciente.nome}!')
            return redirect('pesquisar_consulta')
        except Paciente.DoesNotExist:
            messages.error(request, 'CPF inválido ou não cadastrado.')

    return render(request, 'paciente/login_paciente.html')



def lista_remedios_medico(request):
    
    remedios = Remédio.objects.all()
    return render(request, 'medico/remedios/lista_remedios_medico.html', {'remedios': remedios})

def logout_paciente(request):
    logout(request)
    return redirect('/')

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'medico/pacientes/lista_pacientes.html', {'pacientes': pacientes})

def pesquisar_consulta(request):
    cpf = request.session.get('paciente_cpf')
    
    if cpf:
        try:
            paciente = Paciente.objects.get(cpf=cpf)
            # Busca consultas associadas ao paciente
            consultas = Consulta.objects.filter(id_paciente=paciente)
            return render(request, 'paciente/Pesquisar_consultas.html', {'paciente': paciente, 'consultas': consultas})
        except Paciente.DoesNotExist:
            messages.error(request, 'Erro ao recuperar dados do paciente.')
            return redirect('login_paciente')
    else:
        # Redireciona para login se o CPF não estiver na sessão
        messages.error(request, 'Faça login para acessar esta página.')
        return redirect('login_paciente')



def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                messages.success(request, 'Bem-vindo à área da equipe, superusuário!')
                return redirect('Home') 
            else:
                messages.error(request, 'Você não tem permissão para acessar esta área.')
        else:
            messages.error(request, 'Credenciais inválidas.')
    
    return render(request, 'adm/login.html')

# ---------- Pacientes ---------- 

def pacientes(request):
    return render(request,'adm/pacientes/Pacientes.html',{'pacientes':Paciente.objects.all()}) 

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('pacientes')
        else:
            messages.error(request, 'Erro ao cadastrar o paciente.')
    else:
        form = PacienteForm()
    return render(request, 'adm/pacientes/triagem.html', {'form': form})

def detalharpaciente(request,id):
    return render(request,'adm/pacientes/detalharPaciente.html',{'paciente':Paciente.objects.get(id=id)})

def editarpaciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == "POST":
        paciente.nome = request.POST.get("nome")
        paciente.sintoma = request.POST.get("sintoma")
        paciente.situacao = request.POST.get("situacao")
        paciente.estado_consulta = request.POST.get("estado_consulta")
        paciente.cpf = request.POST.get("cpf")
        paciente.data_nascimento = request.POST.get("data_nascimento")
        paciente.endereco = request.POST.get("endereco")
        paciente.telefone = request.POST.get("telefone")
        paciente.telefone_familiar = request.POST.get("telefone_familiar")
        
        paciente.save()
        return redirect('pacientes')
    
    return render(request, 'adm/pacientes/editarpaciente.html', {'paciente': paciente})

def deletarpaciente(request, id):
    try:
        pacientes = Paciente.objects.get(id=id)
        pacientes.delete()
        return redirect('pacientes')
    except pacientes.DoesNotExist:
        messages.error(request,"Cliente não existe!")
        return redirect('pacientes')
    except ProtectedError:
        messages.error(request,"este paciente nao pode ser deletado")
        return redirect("pacientes")

# ---------- Consultas ---------- 

def consultas(request):
    return render(request,'adm/consultas/Consultas.html',{'consultas':Consulta.objects.all()})

def marcarConsulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.sintoma = consulta.id_paciente.sintoma
            consulta.save()
            messages.success(request, 'Consulta marcada com sucesso')
            return redirect('consultas')
        else:
            messages.error(request, 'Erro ao marcar consulta')
    else:
        form = ConsultaForm()
    return render(request, 'adm/consultas/Marcação.html', {'form': form})

def editarConsulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta editada com sucesso!')
            return redirect('consultas')
        else:
            messages.error(request, 'Erro ao editar consulta.')
    else:
        form = ConsultaForm(instance=consulta)

    return render(request, 'adm/consultas/editarConsulta.html', {'form': form, 'consulta': consulta})

def apagarConsulta(request, id):
    try:
        consulta = Consulta.objects.get(id=id)
        consulta.delete()
        messages.success(request, "Consulta apagada com sucesso!")
        return redirect('consultas')
    
    except Consulta.DoesNotExist:
        messages.error(request, "Consulta não existe!")
        return redirect('consultas')

    
# ---------- Enfermeiros ---------- 

def enfermeiros(request):
    return render(request, 'adm/enfermeiros/enfermeiros.html', {'enfermeiros': Enfermeiro.objects.all()})

def cadastrarEnfermeiro(request):
    if request.method == 'POST':
        form = EnfermeiroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enfermeiro cadastrado com sucesso!')
            return redirect('enfermeiros')
        else:
            messages.error(request, 'Erro ao cadastrar o enfermeiro. Verifique os campos.')
    else:
        form = EnfermeiroForm()
    
    return render(request, 'adm/enfermeiros/cadastrarEnfermeiro.html', {'form': form})

def detalharEnfermeiro(request, id):
    enfermeiro = get_object_or_404(Enfermeiro, id=id)
    
    return render(request, 'adm/enfermeiros/detalharEnfermeiro.html', {'enfermeiro': enfermeiro})

def editarEnfermeiro(request, id):
    enfermeiro = get_object_or_404(Enfermeiro, id=id)

    if request.method == 'POST':
        enfermeiro.nome = request.POST['nome']
        enfermeiro.cpf = request.POST['cpf']
        enfermeiro.disponibilidade = 'disponibilidade' in request.POST
        enfermeiro.contratada = 'contratada' in request.POST
        enfermeiro.endereco = request.POST['endereco']
        enfermeiro.telefone = request.POST['telefone']
        enfermeiro.data_nascimento = request.POST['data_nascimento']
        enfermeiro.data_contratacao = request.POST['data_contratacao']
        enfermeiro.email = request.POST.get('email', '')
        enfermeiro.genero = request.POST.get('genero', '')
        enfermeiro.salario = request.POST.get('salario')
        enfermeiro.turno = request.POST.get('turno' '')
        
        enfermeiro.save()
        return redirect('enfermeiros')

    return render(request, 'adm/enfermeiros/editarEnfermeiro.html', {'enfermeiro': enfermeiro})
# ---------- Médicos ---------- 

def medicos(request):
    return render(request,'adm/medicos/Medicos.html',{'medicos':Médico.objects.all()})
 
def cadastrarMedico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico cadastrado com sucesso!')
            return redirect('medicos')
        else:
            messages.error(request, 'Erro ao cadastrar o médico. Verifique os campos.')
    else:
        form = MedicoForm()
    
    return render(request, 'adm/medicos/cadastrarMedico.html', {'form': form})

def detalharMedico(request, id):
    medico = get_object_or_404(Médico, id=id)
    
    return render(request, 'adm/medicos/detalharMedico.html', {'medico': medico})

def editarMedico(request, id):
    medico = get_object_or_404(Médico, id=id)

    if request.method == 'POST':
        medico.nome = request.POST['nome']
        medico.cpf = request.POST['cpf']
        medico.especializacao = request.POST['especializacao']
        medico.disponibilidade = 'disponibilidade' in request.POST
        medico.contratada = 'contratada' in request.POST
        medico.endereco = request.POST['endereco']
        medico.telefone = request.POST['telefone']
        medico.data_nascimento = request.POST['data_nascimento']
        medico.data_contratacao = request.POST['data_contratacao']
        medico.email = request.POST.get('email', '')
        medico.genero = request.POST.get('genero', '')
        medico.salario = request.POST.get('salario')
        medico.turno = request.POST.get('turno' '')
        
        medico.save()
        return redirect('medicos')

    return render(request, 'adm/medicos/editarMedico.html', {'medico': medico})

# ---------- Remédios ---------- 

def remedios(request):
    return render(request,'adm/remedios/Remedios.html',{'medicamentos':Remédio.objects.all()})
    
def cadastrarRemedio(request):
    if request.method == 'POST':
        form = RemedioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento cadastrado com sucesso!')
            return redirect('remedios')
        else:
            messages.error(request, 'Erro ao cadastrar o medicamento. Verifique os campos.')
    else:
        form = RemedioForm()
    
    return render(request, 'adm/remedios/cadastrarRemedio.html', {'form': form})

def editarRemedio(request, id):
    medicamento = get_object_or_404(Remédio, id=id)

    if request.method == 'POST':
        medicamento.nome = request.POST['nome']
        medicamento.laboratorio = request.POST['laboratorio']
        medicamento.bula = request.POST['bula']
        medicamento.tipo = request.POST['tipo']
        medicamento.quantidade_estoque = request.POST['quantidade_estoque']
        medicamento.data_validade = request.POST['data_validade']
        
        medicamento.save()
        return redirect('remedios')

    return render(request, 'adm/remedios/editarRemedio.html', {'medicamento': medicamento})