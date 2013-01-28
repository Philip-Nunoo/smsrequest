from patientProject.models import Patient, Hospital, Message, Personnel, MessageLog
from django.contrib import admin

class PatientsAdmin (admin.ModelAdmin):
    list_display = ('last_name','telephone_number',)                            #the fields to display in the admin listing page
    list_filter = ('telephone_number','hospital_id',)                                     #the filter method on the right side
    search_fields = ['telephone_number']   

class HospitalsAdmin (admin.ModelAdmin):
    list_display = ('hospital_name',)
    list_filter = ('location',)
    search_fields = ['hospital_name']
    
class MessagesAdmin (admin.ModelAdmin):
    list_display = ('message_type', 'date_created','active','start_at_date', 'message_frequency')
    list_filter = ('message_type', 'date_created','active',)

class PersonnelsAdmin (admin.ModelAdmin):
    list_display = ('first_name','last_name')
    
class MessageLogAdmin (admin.ModelAdmin):
    list_display = ('patient','date_time_sent',)
    list_filter = ('date_time_sent',)
    
admin.site.register(Patient, PatientsAdmin)
admin.site.register(Hospital, HospitalsAdmin)
admin.site.register(Message, MessagesAdmin)
admin.site.register(Personnel, PersonnelsAdmin)
admin.site.register(MessageLog, MessageLogAdmin)