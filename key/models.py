from django.db import models

class Key(models.Model):
    key = models.CharField(max_length = 50, blank = True)
    
    def __unicode__(self):
        return self.key
