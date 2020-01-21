from django.contrib import admin

# Register your models here.

from .models import Property, Category, Reservation

admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Reservation)