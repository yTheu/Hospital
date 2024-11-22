from django.shortcuts import render
from app1.models import Médico, Enfermeira, Paciente, Remédio, Consulta

def index(request):
    return render(request,'index.html')

def triagem(request):
    return render(request,'triagem.html')

def cadastros(request):
    return render(request, 'Cadastro.html')

def medicos(request):
    return render(request,'Medicos.html',{'medico':Médico.objects.all()})

def enfermeiras(request):
    return render(request,'enfermeiras.html',{'enfermeira':Enfermeira.objects.all()})

def pacientes(request):
    return render(request,'Pacientes.html',{'paciente':Paciente.objects.all()})

def remedios(request):
    return render(request,'Remedios.html',{'remedio':Remédio.objects.all()})

def consultas(request):
    return render(request,'Consultas.html',{'consulta':Consulta.objects.all()})