#http://www.djangobook.com/en/2.0/chapter07.html
#http://www.b-list.org/weblog/2006/sep/02/django-tips-user-registration/
from django.forms.models import ModelForm
from patientProject.models import Hospital, Patient, Message, Personnel
from key.models import Key
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.forms.widgets import PasswordInput, Textarea
from django.forms import formsets

class NewPatientForm(ModelForm):
    class Meta:
        model = Patient
        
class NewPersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        
class NewMessageForm(ModelForm):
    class Meta:
        model = Message

class LoginForm(forms.Form):
     username = forms.CharField()
     password = forms.CharField(widget = PasswordInput)
    

class HospitalRegistrationForm(ModelForm):
    class Meta:
        model = Hospital

class KeyForm(forms.Form):
    hospital_key = forms.CharField(label='Key', required = False)
        
def isValidUsername(field_data):
    try:
        User.objects.get(username=field_data)
    except User.DoesNotExist:
        return
    raise validators.ValidationError('The username "%s" is already taken.' % field_data)
    
def AlwaysMatchesOtherField(field1, field2):
    if field1 != field2:
        raise ValidationError(u'Passwords do not match')

class RegistrationForm(forms.Form):
    #def __init__(self):
    first_name = forms.CharField()
    last_name= forms.CharField()
    personnel_type = forms.CharField()
    email = forms.EmailField(required = False, help_text='A valid email address, please.')
    
    username = forms.CharField(validators = [isValidUsername])
    password = forms.CharField(widget = PasswordInput)
    verify_password = forms.CharField(widget = PasswordInput)#, validators = [AlwaysMatchesOtherField])
    #verify_password = forms.CharField(widget = PasswordInput)