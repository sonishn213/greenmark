  
from django.contrib import admin
from .models import PortfolioDetails
# Register your models here.


class PortfolioDetailsAdmin(admin.ModelAdmin):
    list_display = ('title','image','content','Mainimage','image1','image2','image3','image4','image5','image6')
    search_fields = ('title',)




admin.site.register(PortfolioDetails,PortfolioDetailsAdmin)

# Register your models here.
