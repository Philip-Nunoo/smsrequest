from django.contrib import admin
from key.models import Key

class KeyAdmin (admin.ModelAdmin):
    list_display = ('key',)
    
admin.site.register(Key,KeyAdmin)
