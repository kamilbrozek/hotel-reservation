from django.db import models
from datetime import date

# Create your models here.

#class Contact(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    email = models.EmailField()
#    message = models.TextField()
#    today = str(date.today())
#    def __str__(self):
#        return str(self.first_name+'_'+self.last_name+'_'+today)

class ContactInformation(models.Model):
    location = ""
    tel = models.CharField(max_length=15)
    email = models.EmailField()
    address= models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

# Add contact details instead contact