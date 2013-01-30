from django.forms.models import ModelForm
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput, Textarea
from django.contrib.auth.models import User

from public.models import Hospital

def AlwaysMatchesOtherField(field1, field2):
    if field1 != field2:
        raise ValidationError(u'Passwords do not match')
        
def isValidUsername(field_data):
		try:
			User.objects.get(username=field_data)
		except User.DoesNotExist:
			return
		raise validators.ValidationError('The username "%s" is already taken.' % field_data)
		
class HospitalRegistrationForm(ModelForm):
    class Meta:
        model = Hospital
        
class UserRegistrationForm(forms.Form):
    #def __init__(self):
    first_name = forms.CharField()
    last_name= forms.CharField()
    personnel_type = forms.CharField()
    email = forms.EmailField(required = False, help_text='A valid email address, please.')
    
    username = forms.CharField(validators = [isValidUsername])
    password = forms.CharField(widget = PasswordInput)
    verify_password = forms.CharField(widget = PasswordInput)#, validators = [AlwaysMatchesOtherField])
    #verify_password = forms.CharField(widget = PasswordInput)
    
	
