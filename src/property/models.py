from django.db import models

# Create your models here.

property_type =(
    ('S', "sale"),
    ('R', "rent")
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    #location
    property_type = models.CharField(choices=property_type,max_length=10)
    price = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places=2, max_digits=5)
    beds_number = models.PositiveIntegerField()
    bath_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/',null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
    

# Category Model

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'