from django.shortcuts import render
from .models import Grid
from contactus.models import Contact
from django.core.mail import send_mail,BadHeaderError
def home_view(request):
    imgs = Grid.objects.all().order_by('?')[:6]
    if request.method == "POST":
        cont = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        services = request.POST.get('services')
        message=request.POST.get('message')
        cont.name=name
        cont.email=email
        cont.phonenumber=phonenumber
        cont.services = services
        cont.message=message
        cont.save()
        subject = "Website Inquiry"
        body = {
            'name': name,
            'phonenumber': phonenumber,
            'email':  email,
            'message':  message,
        }
        MESSAGE = "\n".join(body.values())
        send_mail(
            subject,
            MESSAGE,
            'hellocrys6@gmail.com',
            ['sarahcrystal21@gmail.com']
        )
    return render(request, 'home/Portfolio.html',{'imgs':imgs})
