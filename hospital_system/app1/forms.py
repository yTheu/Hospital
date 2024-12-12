from django import forms
from app1.models import Paciente, Consulta, Médico, Enfermeiro, Remédio

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sintoma', 'situacao', 'estado_consulta', 'cpf', 'data_nascimento', 'endereco', 'telefone', 'telefone_familiar']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Paciente.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Já existe um paciente com este CPF.')
        return cpf

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        if self.instance and self.instance.estado_consulta == 'Triagem':
            self.fields['estado_consulta'].widget = forms.HiddenInput()

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Médico
        fields = ['nome', 'cpf', 'especializacao', 'disponibilidade', 'contratada', 'data_nascimento', 'endereco', 'telefone', 'email', 'genero', 'salario', 'turno', 'data_contratacao']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Médico.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Já existe um médico com este CPF.')
        return cpf


class EnfermeiroForm(forms.ModelForm):
    class Meta:
        model = Enfermeiro
        fields = ['nome', 'cpf', 'disponibilidade', 'contratada', 'endereco', 'telefone', 'data_nascimento', 'email', 'genero', 'salario', 'turno', 'data_contratacao']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Enfermeiro.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Já existe uma enfermeiro com este CPF.')
        return cpf

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['disponibilidade'].widget = forms.HiddenInput()
        self.fields['contratada'].widget = forms.HiddenInput()

class RemedioForm(forms.ModelForm):
    class Meta:
        model = Remédio
        fields = ['nome', 'laboratorio', 'bula', 'tipo', 'quantidade_estoque', 'data_validade']

    

    data_validade = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['id_paciente', 'sintoma', 'id_enfermeiro', 'id_medico', 'id_medicação', 'data_consulta']

    data_consulta = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )