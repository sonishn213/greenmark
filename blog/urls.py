from django.urls import path, re_path
from .import views
app_name = 'blog'
urlpatterns = [
path('', views.bloggrid_view,name='grid'),
path('<str:Url>/', views.article_details, name='detail'),
]