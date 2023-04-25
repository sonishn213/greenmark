from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
def contact_view(request):
    msg = {
        "status": "success"
    }
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
        cont.services=services
        cont.message=message
        cont.save()
        subject = "Website Inquiry"
        body = {
            'name': name,
            'phonenumber': phonenumber,
            'email': email,
            'message': message,
        }
        MESSAGE= "\n".join(body.values())
        try:
            send_mail(
                subject,
                MESSAGE,
                'hellocrys6@gmail.com',
                ['sarahcrystal21@gmail.com']
            )
            msg["status"] = "success"
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contactus/',msg)


    return render(request, 'contactus/Contactus.html',msg)
