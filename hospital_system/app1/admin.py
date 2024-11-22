from django.contrib import admin
from app1.models import Paciente, Médico, Secretária, Remédio, Consulta

admin.site.register(Paciente)
admin.site.register(Médico)
admin.site.register(Secretária)
admin.site.register(Remédio)
admin.site.register(Consulta)