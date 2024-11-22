from django.contrib import admin
from app1.models import Paciente, Médico, Enfermeira, Remédio, Consulta

admin.site.register(Paciente)
admin.site.register(Médico)
admin.site.register(Enfermeira)
admin.site.register(Remédio)
admin.site.register(Consulta)