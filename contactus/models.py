from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, default=None)
    phonenumber = models.CharField(max_length=10)
    services = models.TextField()

    message = models.TextField()

    def __str__(self):
        return self.name


