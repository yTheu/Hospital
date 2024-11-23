from django.contrib import admin
from django.urls import path
from app1.views import index, triagem, medicos, enfermeiras, pacientes, remedios, consulta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('in', index),
    path('triagem', triagem, name="triagem"),
    path('medicos', medicos, name="medicos"),
    path('enfermeiras', enfermeiras, name='enfermeiras'),
    path('pacientes', pacientes, name="pacientes"),
    path('remedios', remedios,name='remedios'),
    path('consulta', consulta,name='consulta')
]
