from django.contrib import admin
from django.urls import path
from app1.views import index, custom_login, editarConsulta, apagarConsulta, medicos, enfermeiras, pacientes, remedios, consulta, cadastrar_usuario, detalharpaciente,marcarConsulta,editarRemedio,editarpaciente
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff', custom_login, name='staff'),
    path('', index),

    path('pacientes', pacientes, name="pacientes"),
    path('detalharPaciente/<int:id>',detalharpaciente,name='detalharPaciente'),
    path('editarpaciente/<int:id>',editarpaciente,name='editarpaciente'),

    path('triagem', cadastrar_usuario, name='cadastrar_usuario'),
    path('consulta', consulta,name='consulta'),
    path('marcarconsulta',marcarConsulta,name='marcarconsulta'),
    path('editarConsulta/<int:id>', editarConsulta, name='editarConsulta'),
    path('apagarConsulta/<int:id>', apagarConsulta, name='apagarConsulta'),

    path('enfermeiras', enfermeiras, name='enfermeiras'),

    path('medicos', medicos, name="medicos"),

    path('remedios', remedios,name='remedios'),
    path('editarRemedio/<int:id>', editarRemedio, name='editarRemedio')

]