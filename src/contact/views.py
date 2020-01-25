from django.shortcuts import render, redirect
from .models import ContactInformation
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def contact(request):
    contactInfo = ContactInformation.objects.last()
    contactForm = ContactForm()
    template = 'contact/contact.html'

    if request.method == 'POST' :
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            subject = contactForm.cleaned_data['subject']
            from_email = contactForm.cleaned_data['email_from']
            message = contactForm.cleaned_data['message']
            try:
                send_mail(subject,message,from_email,['test@gmail.com'])

            except BadHeaderError :
                return HttpResponse("invalid header")
            return redirect('contact:success')
        else:
            contactForm=  ContactForm()


    context = {
        'contactInfo' : contactInfo,
        'contactForm' : contactForm
    }
    return render(request,template,context)

def success(request):
    return HttpResponse("Email Sent Succesfully")