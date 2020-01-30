from django.shortcuts import render
from .models import Property, Category
from .forms import ReservationForms
from django.db.models import Q


# Create your views here.


def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'
    address_querry = request.GET.get('q')
    property_type = request.GET.getlist("selectForm" , None)
    print(address_querry)
    print(property_type)
    if address_querry and property_type:
        print(address_querry)
        print(property_type)
        property_list = property_list.filter(
            Q(name__icontains = address_querry ) & 
            Q(property_type__icontains = property_type[0])
        ).distinct()
    else:
        print("brak")
        
    context = {
        'property_list' : property_list
    }
    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/details.html'

    if request.method == 'POST':
        reserve_form=ReservationForms(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReservationForms(); 

    context = {
        'property_detail' : property_detail,
        'reserve_form'    : reserve_form
    }
    return render(request, template, context)