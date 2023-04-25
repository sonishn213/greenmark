from django.urls import path, re_path
from .import views
app_name = 'contactus'
urlpatterns = [
path('', views.contact_view,name='reach'),

]