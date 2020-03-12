from django.db import models


# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name
