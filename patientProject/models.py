from django.db import models
from django.contrib.auth.models import User
from django.forms.models import ModelForm

TYPES_LIST = (
    ('Health Tip','Health Tip'),
    ('Appointment','Appointment'),
    ('General Information','General Information'),
)

FREQUENCY = {
    ('once', 'This Time Only'),
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('specify', 'Specify date to send message')
}

# Create your models here.

class Hospital(models.Model):
    hospital_name = models.CharField(max_length = 60)
    postal_address = models.TextField()
    location = models.CharField(max_length = 50)
    email = models.EmailField()
    contact_number = models.CharField(max_length = 15)
    
    def __unicode__(self):
        return self.hospital_name
    
class Personnel(models.Model):
    first_name = models.CharField(max_length = 50) #
    last_name = models.CharField(max_length = 50) #
    personnel_type = models.CharField(max_length = 50) #
    email = models.EmailField()
    
    activation_key = models.CharField(max_length = 40) # ....
    key_expires = models.DateTimeField() # .....
    
    hospital = models.ForeignKey(Hospital) #
    user = models.OneToOneField(User)
    
    def __unicode___(self):
        return self.personnel_name

class Patient(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    telephone_number = models.CharField(max_length = 10)
    email_address = models.EmailField(blank = True)
    registration_date = models.DateField(auto_now = True)
    
    hospital_id = models.ForeignKey(Hospital)
    description = models.TextField()
    
    def __unicode__(self):
        return self.first_name
    
class Message(models.Model):
    receipient_name = models.ForeignKey(Patient)
    message_content = models.TextField()
    message_frequency = models.CharField(max_length=20, choices = FREQUENCY)
    active = models.BooleanField(default = True)
    
    start_at_date = models.DateField(blank = True)
    end_at_date = models.DateField(blank = True)
    date_created = models.DateField(auto_now = True)
    
    message_type = models.CharField(max_length = 50, choices = TYPES_LIST)
    
    def __unicode__(self):
        return self.message_type

class MessageLog(models.Model):
    message = models.ForeignKey(Message)
    patient = models.ForeignKey(Patient)
    date_time_sent = models.DateTimeField(auto_now = True)