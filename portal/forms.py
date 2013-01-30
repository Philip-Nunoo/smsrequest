from django.forms.models import ModelForm

from portal.models import Message, Patient
from public.models import Personnel

class NewMessageForm(ModelForm):
	class Meta:
		model = Message

class NewPatientForm(ModelForm):
	class Meta:
		model = Patient
		
class NewPersonnelForm(ModelForm):
	class Meta:
		model = Personnel
