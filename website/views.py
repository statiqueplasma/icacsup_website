from django.shortcuts import render
from django.contrib import messages
from .models import articles, metiers, programmes, details
from django.core.mail import send_mail
from django.views.generic import DetailView, ListView
# Create your views here.

class HomeView(ListView):
    model = articles
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['metiers'] = metiers.objects.all()
        context['programmes'] = programmes.objects.all()
        context['details'] = details.objects.all()
        return context
    
class ArticleView(DetailView):
    model = articles
    template_name = 'article.html'

class MetierListView(ListView):
    model = metiers
    template_name = 'metiers_list.html'    

class MetierView(DetailView):
    model = metiers
    template_name = 'metier.html'

class programmeListView(ListView):
    model = programmes
    template_name = 'programmes_list.html'

class ProgrammeView(DetailView):
    model = programmes
    template_name = 'programme_lic.html'
class masterView(DetailView):
    model = programmes
    template_name = 'programme_mas.html'

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