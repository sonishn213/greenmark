from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog_grid,Blog_details
from django.core.paginator import Paginator
# Create your views here.

def bloggrid_view(request):
    articles = Blog_grid.objects.all().order_by('add_date')
    p=Paginator(Blog_grid.objects.all(),6)
    page=request.GET.get('page')
    blogs_grid=p.get_page(page)
    return render(request, 'blog/Blog.html', {'articles': articles,'blogs_grid':blogs_grid})
def article_details(request,Url):
    # return HttpResponse(slug)
    BLOG = Blog_details.objects.get(Url=Url)

    related=Blog_grid.objects.filter(category=BLOG.Url.category).exclude(Url=Url)

    return render(request, 'blog/blogdetails.html', {'BLOG': BLOG,'related':related})
