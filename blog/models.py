from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField




# Create your models here.
class Blog_grid(models.Model):
    Url = models.CharField(max_length=255,primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    image = models.ImageField(default="default.png",blank=True,upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(max_length=50, default=None)
    category = models.CharField(max_length=50, default=None)





    def __str__(self):
        return self.Url

    def snippet(self):
        return self.description[:150]+ "..."


    def day(self):
        return self.add_date.strftime('%d')
    def month(self):
        return self.add_date.strftime('%b')
    def year(self):
        return self.add_date.strftime('%Y')




class Blog_details(models.Model):
    Url = models.ForeignKey(Blog_grid, on_delete=models.CASCADE, related_name="Urls")
    content = RichTextField()
    quote=models.TextField()
    quoteauthor=models.CharField(max_length=100)
    othimage = models.ImageField(default="default.png",blank=True,upload_to='post/')
    authorpic=models.ImageField(default="default.png",blank=True,upload_to='post/')
    aboutauthor=models.TextField()
    fb_url=models.CharField(max_length=255,default=None)
    t_url=models.CharField(max_length=255,default=None)
    insta_url=models.CharField(max_length=255,default=None)




















