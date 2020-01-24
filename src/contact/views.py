from django.shortcuts import render
from .models import Contact
# Create your views here.

def contact(request):
    contacts = Contact.objects.all()
    template = 'contact/contact.html'
    context = {
        'contacts' : contacts
    }
    return render(request,template,context)