from django.shortcuts import render
from property.models import Property, Category

# Create your views here.


def home(request):
    category_list = Category.objects.all()
    template = 'home/index.html'
    context = {
        'category_list'  : category_list,
     }
    return render(request,template,context)