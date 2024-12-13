from django.contrib import admin
from django.urls import path
from app1.views import (
    index, custom_login, home, login_paciente, logout_paciente, login_medico,
    agenda_medica, pesquisar_consulta, editar_consulta_medico, detalhar_consulta_medico,
    lista_pacientes, lista_remedios_medico, editarConsulta, cadastrar_usuario, pacientes,
    detalharpaciente, editarpaciente, consultas, marcarConsulta, editarRemedio, editarpaciente,
    enfermeiros, cadastrarEnfermeiro, detalharEnfermeiro, editarEnfermeiro, medicos,
    cadastrarMedico, detalharMedico, editarMedico, remedios, cadastrarRemedio, apagarConsulta
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Página inicial
    path('', index),
    path('Home', home, name='Home'),

    # Autenticação
    path('staff/', custom_login, name='staff'),
    path('login_paciente/', login_paciente, name='login_paciente'),
    path('logout_paciente/', logout_paciente, name='logout_paciente'),
    path('login_medico/', login_medico, name='login_medico'),

    # Área Médica
    path('agenda_medica/', agenda_medica, name='agenda_medica'),
    path('detalhar_consulta_medico/<int:id>/', detalhar_consulta_medico, name='detalhar_consulta_medico'),
    path('editar_consulta_medico/<int:id>/', editar_consulta_medico, name='editar_consulta_medico'),
    
    path('lista_pacientes/', lista_pacientes, name='lista_pacientes'),
    path('lista_remedios/', lista_remedios_medico, name='lista_remedios_medico'),

    # Área do paciente
    path('pesquisar_consulta', pesquisar_consulta, name='pesquisar_consulta'),

    # Consultas
    path('consultas/', consultas, name='consultas'),
    path('marcarconsulta/', marcarConsulta, name='marcarconsulta'),
    path('editarConsulta/<int:id>/', editarConsulta, name='editarConsulta'),
    path('apagarConsulta/<int:id>/', apagarConsulta, name='apagarConsulta'),

    # Pacientes
    path('pacientes/', pacientes, name="pacientes"),
    path('detalharPaciente/<int:id>/', detalharpaciente, name='detalharPaciente'),
    path('editarpaciente/<int:id>/', editarpaciente, name='editarpaciente'),

    # Remédios
    path('remedios/', remedios, name='remedios'),
    path('cadastrarRemedio/', cadastrarRemedio, name='cadastrarRemedio'),
    path('editarRemedio/<int:id>/', editarRemedio, name='editarRemedio'),

    # Enfermeiros
    path('enfermeiros/', enfermeiros, name='enfermeiros'),
    path('cadastrarEnfermeiro/', cadastrarEnfermeiro, name='cadastrarEnfermeiro'),
    path('detalharEnfermeiro/<int:id>/', detalharEnfermeiro, name='detalharEnfermeiro'),
    path('editarEnfermeiro/<int:id>/', editarEnfermeiro, name='editarEnfermeiro'),

    # Médicos
    path('medicos/', medicos, name="medicos"),
    path('cadastrarMedico/', cadastrarMedico, name='cadastrarMedico'),
    path('detalharMedico/<int:id>/', detalharMedico, name='detalharMedico'),
    path('editarMedico/<int:id>/', editarMedico, name='editarMedico'),

    # Cadastro de Usuário
    path('triagem/', cadastrar_usuario, name='cadastrar_usuario'),
]
