from django import forms
from app1.models import Paciente

class UsuarioForm(forms.ModelForm):
  

 class Meta:
        model = Paciente
        fields = ['nome', 'sintoma', 'situacao','cpf','data_nascimento','endereco','telefone','telefone_familiar']