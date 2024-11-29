from django.shortcuts import render,redirect
from app1.models import Médico, Enfermeira, Paciente, Remédio, Consulta
from app1.forms import UsuarioForm, outroForm
from django.contrib import messages
from django.db.models.deletion import ProtectedError

def index(request):
    return render(request,'index.html')


def consultas(request):
    return render(request, 'Consultas.html')

def medicos(request):
    return render(request,'Medicos.html',{'medico':Médico.objects.all()})

def enfermeiras(request):
    return render(request,'enfermeiras.html',{'enfermeira':Enfermeira.objects.all()})

def pacientes(request):
    return render(request,'Pacientes.html',{'paciente':Paciente.objects.all()}) 

def detalharpaciente(request,id):
    return render(request,'detalharPaciente.html',{'paciente':Paciente.objects.get(id=id)})

def remedios(request):
    return render(request,'Remedios.html',{'remedio':Remédio.objects.all()})

def consulta(request):
    return render(request,'Consultas.html',{'consulta':Consulta.objects.all()})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Criptografar a senha antes de salvar
            usuario.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('cadastrar_usuario')
        else:
            messages.error(request, 'Erro ao cadastrar o paciente.')
    else:
        form = UsuarioForm()
    return render(request, 'triagem.html', {'form': form})

def marcarConsulta(request):
    if request.method == 'POST':

        form = outroForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            # Criptografar a senha antes de salvar
            consulta.save()
            messages.success(request, 'consulta marcada com sucesso')
            return redirect('cadastrar_usuario')
        else:
            messages.error(request, 'Erro ao marcar consulta')
    else:
        form = outroForm()
    return render(request, 'marcação.html', {'form': form})

def deletarpaciente(request, id):
    try:
        pacientes = Paciente.objects.get(id=id)
        pacientes.delete()
        return redirect('pacientes')
    except pacientes.DoesNotExist:
        messages.error(request,"Cliente não existe!")
        return redirect('lpacientes')
    except ProtectedError:
        messages.error(request,"este paciente nao pode ser deletado")
        return redirect("pacientes")
    
def editarpaciente(request,id):
    pacientes = Paciente.objects.get(id=id)
    if request.method == "POST":
        pacientes.nome = request.POST.get("nome")
        pacientes.sintoma = request.POST.get("sintoma")
        pacientes.situação = request.POST.get("situação")
        pacientes.cpf = request.POST.get("cpf")
        pacientes.data_nascimento = request.POST.get("data_nascimento")
        pacientes.endereco = request.POST.get("endereco")
        pacientes.telefone= request.POST.get("telefone")
        pacientes.telefone_familiar= request.POST.get("telefone_familiar")
        
        pacientes.save()
        return redirect('pacientes')
    else:
        return render(request,'editarpaciente.html',{'pacientes':pacientes})