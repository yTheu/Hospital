from django.contrib import admin
from django.urls import path
from app1.views import index, custom_login, medicos, enfermeiras, pacientes, remedios, consulta, cadastrar_usuario, detalharpaciente,marcarConsulta,deletarpaciente,editarpaciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('in', index),
    path('staff/', custom_login, name='staff'),
    path('medicos', medicos, name="medicos"),
    path('triagem', cadastrar_usuario, name='cadastrar_usuario'),
    path('enfermeiras', enfermeiras, name='enfermeiras'),
    path('pacientes', pacientes, name="pacientes"),
    path('remedios', remedios,name='remedios'),
    path('consulta', consulta,name='consulta'),
    path('detalharPaciente/<int:id>',detalharpaciente,name='detalharPaciente'),
    path('marcarconsulta',marcarConsulta,name='marcarconsulta'),
    path('deletarpaciente/<int:id>',deletarpaciente,name='deletarpaciente'),
    path('editarpaciente/<int:id>',editarpaciente,name='editarpaciente')
]