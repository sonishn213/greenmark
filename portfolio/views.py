from django.shortcuts import render
from home.models import Grid
from portfolio.models import PortfolioDetails

# Create your views here.
def portfolio_view(request):
    AllImages=Grid.objects.all()
    return render(request, 'portfolio/allportfolio.html',{'AllImages':AllImages})

def portfoilo_details(request,title):
   portdet=PortfolioDetails.objects.get(title__title=title)
   imgs = Grid.objects.all().order_by('?')[:6]
   return render(request, 'portfolio/portfolio-details.html', {'portdet':portdet,'imgs':imgs})

