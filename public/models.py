from django.db import models
from django.contrib.auth.models import User
	
class Hospital(models.Model):
    hospital_name = models.CharField(max_length = 60)
    postal_address = models.TextField()
    location = models.CharField(max_length = 50)
    email = models.EmailField()
    contact_number = models.CharField(max_length = 15)
    
    def __unicode__(self):
        return self.hospital_name

class Personnel(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    personnel_type = models.CharField(max_length = 50)
    email = models.EmailField()
    
    activation_key = models.CharField(max_length = 40)
    key_expires = models.DateTimeField()
    
    hospital = models.ForeignKey(Hospital)
    user = models.OneToOneField(User)
    
    def __unicode___(self):
        return self.personnel_name
