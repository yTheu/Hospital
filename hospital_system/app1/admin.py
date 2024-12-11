from django.contrib import admin
from app1.models import Paciente, Médico, Enfermeiro, Remédio, Consulta

admin.site.register(Paciente)
admin.site.register(Médico)
admin.site.register(Enfermeiro)
admin.site.register(Remédio)
admin.site.register(Consulta)