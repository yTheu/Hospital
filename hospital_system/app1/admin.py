from django.contrib import admin
from models import Paciente, Medico, Secretaria, Remedio, Consulta

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Secretaria)
admin.site.register(Remedio)
admin.site.register(Consulta)