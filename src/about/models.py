from django.db import models

# Create your models here.


class About(models.Model):

    ourVision = models.TextField(max_length=300)
    ourMission = models.TextField(max_length=300)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return str(self.id)