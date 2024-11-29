from django.shortcuts import render,redirect
from app1.models import Médico, Enfermeira, Paciente, Remédio, Consulta
from app1.forms import UsuarioForm, outroForm
from django.contrib import messages

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