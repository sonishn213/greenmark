from django.urls import path, re_path
from .import views
app_name = 'aboutus'
urlpatterns = [
path('', views.aboutus_view,name='reach'),

]