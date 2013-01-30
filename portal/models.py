from django.db import models
from public.models import Hospital

FREQUENCY = {
    ('once', 'This Time Only'),
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('specify', 'Specify date to send message')
}

TYPES_LIST = (
    ('Health Tip','Health Tip'),
    ('Appointment','Appointment'),
    ('General Information','General Information'),
)
    
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
    date_time_sent = models.DateTimeField(auto_now = True, auto_now_add=True)
    
    def __unicode__(self):
        return self.first_name
