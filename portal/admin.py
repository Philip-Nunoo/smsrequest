from django.contrib import admin
from portal.models import Patient, Message, MessageLog

class MessageLogAdmin (admin.ModelAdmin):
	fieldsets = []
	list_display = ('message','patient','date_time_sent')
	#list_filter = ('message_type','message_week')
	search_fields = ['patient'] 

class MessageAdmin (admin.ModelAdmin):
	list_display = ('receipient_name', 'message_frequency','start_at_date','active',)
	list_filter = ('start_at_date',)
	
admin.site.register(Patient)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageLog, MessageLogAdmin)
