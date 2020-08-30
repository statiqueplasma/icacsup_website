from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['contact-fname']
        contact_lname = request.POST['contact-lname']
        contact_mail = request.POST['contact-mail']
        contact_tel = request.POST['contact-tel']
        contact_message = request.POST['contact-message']
        send_mail(
            "website contact",
            "message de :" + contact_lname + contact_fname + '|' + 'tel: ' + contact_tel + '/n' + "--------------------------" + '/n' + contact_message,
            contact_mail,
            ['hay.aouadidrissi@gmail.com']
        )
        messages.success(request, 'Votre E-mail a bien été envoyé au nom de : <b>{} {}</b>'.format(contact_lname,contact_fname))
        return render(request, 'contact.html', {})
    else:
        return render(request, 'contact.html', {})