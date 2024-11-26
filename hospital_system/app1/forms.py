from django import forms
from app1.models import Paciente

class UsuarioForm(forms.ModelForm):
  

 class Meta:
        model = Paciente
        fields = ['nome', 'sintoma', 'situacao','cpf','data_nascimento','endereco','telefone','telefone_familiar']
def clean_email(self):
        
 cpf = self.cleaned_data.get('cpf')
 if Paciente.objects.filter(cpf=cpf).exists():
   raise forms.ValidationError('Já existe um paciente com este cpf.')
 return cpf