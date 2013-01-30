from django.contrib import admin
from public.models import Hospital, Personnel

admin.site.register(Hospital)
admin.site.register(Personnel)
'''
admin.site.register(Patient, PatientsAdmin)
admin.site.register(Hospital, HospitalsAdmin)
admin.site.register(Message, MessagesAdmin)
admin.site.register(Personnel, PersonnelsAdmin)
admin.site.register(MessageLog, MessageLogAdmin)
'''
