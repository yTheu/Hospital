from django.shortcuts import render,redirect
from app1.models import Médico, Enfermeira, Paciente, Remédio, Consulta
from app1.forms import UsuarioForm

def index(request):
    return render(request,'index.html')

#def triagem(request):
  #  return render(request,'triagem.html')

def consultas(request):
    return render(request, 'Consultas.html')

def medicos(request):
    return render(request,'Medicos.html',{'medico':Médico.objects.all()})

def enfermeiras(request):
    return render(request,'enfermeiras.html',{'enfermeira':Enfermeira.objects.all()})

def pacientes(request):
    return render(request,'Pacientes.html',{'paciente':Paciente.objects.all()})

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
            
            return redirect('cadastrar_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'cadastros.html', {'form': form})