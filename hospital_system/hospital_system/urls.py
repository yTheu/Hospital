from django.contrib import admin
from django.urls import path
from app1.views import index, medicos,triagem, enfermeiras, pacientes, remedios, consulta, cadastrar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('in', index),
   # path('triagem', triagem, name="triagem"),
    path('medicos', medicos, name="medicos"),
    path('triagem', cadastrar_usuario, name='triagem'),
    path('enfermeiras', enfermeiras, name='enfermeiras'),
    path('pacientes', pacientes, name="pacientes"),
    path('remedios', remedios,name='remedios'),
    path('consulta', consulta,name='consulta')
]
