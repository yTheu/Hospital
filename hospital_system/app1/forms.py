from django import forms
from app1.models import Paciente, Consulta

class UsuarioForm(forms.ModelForm):
  

 class Meta:
        model = Paciente
        fields = ['nome', 'sintoma', 'situacao','cpf','data_nascimento','endereco','telefone','telefone_familiar']
def clean_email(self):
        
 cpf = self.cleaned_data.get('cpf')
 if Paciente.objects.filter(cpf=cpf).exists():
   raise forms.ValidationError('Já existe um paciente com este cpf.')
 return cpf

class outroForm(forms.ModelForm):
  

 class Meta:
        model = Consulta
        fields = ['id_paciente', 'doença','id_enfermeira','id_medico','id_medicação']

        