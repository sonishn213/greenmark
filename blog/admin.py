from django.contrib import admin
from .models import Blog_grid,Blog_details
# Register your models here.


class BloggridAdmin(admin.ModelAdmin):
    list_display = ('Url','title','description','add_date','image','author','category')
    search_fields = ('title',)
    list_filter = ('author','category')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('content','quote','quoteauthor','othimage','authorpic','aboutauthor','fb_url','t_url','insta_url',)
    search_fields = ('title',)


admin.site.register(Blog_details,BlogAdmin)

admin.site.register(Blog_grid,BloggridAdmin)

