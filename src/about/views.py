from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):
    about = About.objects.first()
    template = 'about/about.html'
    context = {
        'about' : about
    }
    return render(request,template,context)