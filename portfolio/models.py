from django.db import models
from home.models import Grid
from ckeditor.fields import RichTextField


# Create your models here.
class PortfolioDetails(models.Model):

    image = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    content = RichTextField()
    Mainimage = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    image1 = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    image2 = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    image3 = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    image4 = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    image5 = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    image6 = models.ImageField(default="default.png", blank=True, upload_to='grid/')
    title = models.ForeignKey(Grid, on_delete=models.CASCADE)
