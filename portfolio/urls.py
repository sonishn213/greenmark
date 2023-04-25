from django.urls import path, re_path
from .import views
app_name = 'allport'
urlpatterns = [
path('', views.portfolio_view,name='Portfolio'),
path('<str:title>/', views.portfoilo_details, name='portdetail'),
]