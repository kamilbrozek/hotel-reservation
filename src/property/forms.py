from django import forms
from .models import Reservation, Property

class ReservationForms(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
    
class PropertySearch(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'