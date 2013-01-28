from key.models import Key
from django.contrib import admin

class KeyAdmin (admin.ModelAdmin):
    list_display = ('hospital_name','hospital_key')
    
admin.site.register(Key, KeyAdmin)