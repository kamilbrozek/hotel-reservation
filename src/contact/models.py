from django.db import models
from datetime import date

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    today = str(date.today())

    def __str__(self):
        return str(self.first_name+'_'+self.last_name+'_'+today)


# Add contact details instead contact