from django.db import models
from patientProject.models import Hospital
# Create your models here.

class Key(models.Model):
    hospital_name = models.ForeignKey(Hospital)
    #hospital_id = models.CharField(max_length = 40, blank = True)
    hospital_key = models.CharField(max_length = 50, blank = True)
    
    def __unicode__(self):
        return self.hospital_key