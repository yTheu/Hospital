from django.contrib import admin
from django.urls import path
from app1.views import index, custom_login, editarConsulta, detalharEnfermeiro, cadastrarRemedio, editarMedico, detalharMedico, cadastrarMedico, cadastrarEnfermeiro, editarEnfermeiro, apagarConsulta, medicos, enfermeiros, pacientes, remedios, consultas, cadastrar_usuario, detalharpaciente, marcarConsulta, editarRemedio, editarpaciente, home, login_medico, login_paciente, agenda_medica, pesquisar_consulta
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', custom_login, name='staff'),
    path('', index),
    path('Home', home, name='Home'),
    path('login_paciente', login_paciente, name='login_paciente'),
    path('login_medico', login_medico, name='login_medico'),
    path('agenda_medica', agenda_medica, name='agenda_medica'),
    path('pesquisar_consulta', pesquisar_consulta, name='pesquisar_consulta'),


    path('triagem', cadastrar_usuario, name='cadastrar_usuario'),
    path('pacientes', pacientes, name="pacientes"),
    path('detalharPaciente/<int:id>', detalharpaciente, name='detalharPaciente'),
    path('editarpaciente/<int:id>', editarpaciente, name='editarpaciente'),

    path('consultas', consultas, name='consultas'),
    path('marcarconsulta', marcarConsulta, name='marcarconsulta'),
    path('editarConsulta/<int:id>', editarConsulta, name='editarConsulta'),
    path('apagarConsulta/<int:id>', apagarConsulta, name='apagarConsulta'),

    path('enfermeiros', enfermeiros, name='enfermeiros'),
    path('cadastrarEnfermeiro', cadastrarEnfermeiro, name='cadastrarEnfermeiro'),
    path('detalharEnfermeiro/<int:id>',
         detalharEnfermeiro, name='detalharEnfermeiro'),
    path('editarEnfermeiro/<int:id>', editarEnfermeiro, name='editarEnfermeiro'),

    path('medicos', medicos, name="medicos"),
    path('cadastrarMedico', cadastrarMedico, name='cadastrarMedico'),
    path('detalharMedico/<int:id>', detalharMedico, name='detalharMedico'),
    path('editarMedico/<int:id>', editarMedico, name='editarMedico'),

    path('remedios', remedios, name='remedios'),
    path('cadastrarRemedio', cadastrarRemedio, name='cadastrarRemedio'),
    path('editarRemedio/<int:id>', editarRemedio, name='editarRemedio')

]
