from django.contrib import admin
from portal.models import Patient, Message, MessageLog

admin.site.register(Patient)
admin.site.register(Message)
admin.site.register(MessageLog)
