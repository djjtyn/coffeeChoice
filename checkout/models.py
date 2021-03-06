from django.db import models
from coffee.models import Coffee


# Create your models here.
#Order model which has user details
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

#Orderline details which contain coffee details and quantities
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    coffee = models.ForeignKey(Coffee, null=False)
    quantity = models.IntegerField(blank=False)
    

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.coffee.name, self.coffee.price)