from django.contrib import admin
from .models import Grid
# Register your models here.


class GridAdmin(admin.ModelAdmin):
    list_display = ('title','image','category')
    search_fields = ('title',)
    list_filter = ('category',)



admin.site.register(Grid,GridAdmin)