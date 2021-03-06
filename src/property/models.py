from django.db import models

# Create your models here.

property_types =(
    ('Sale', "sale"),
    ('Rent', "rent")
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True)
    property_type = models.CharField(choices=property_types,max_length=10)
    price = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places=2, max_digits=5)
    beds_number = models.PositiveIntegerField()
    bath_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/',null=True)
    details = models.TextField(max_length= 300)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
    

# Category Model

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/',null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    descryption = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    