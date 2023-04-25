from django.contrib import admin

# Register your models here.
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phonenumber','services','message',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Contact,ContactAdmin)