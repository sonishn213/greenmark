from django.db import models

class Grid(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    category = models.CharField(max_length=50)


    def __str__(self):
        return self.title

    
