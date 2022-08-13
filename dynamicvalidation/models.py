from django.db import models
from django.core.exceptions import ValidationError

class Item(models.Model):
    name = models.CharField(max_length=100)
    minbid = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name + ' - ' + str(self.minbid)

def min_bid_validator(value):
    """ This works for static values, but how do I say value < item.minbid? """
    if value < 10:
        raise ValidationError('Bid must be at least $10')

from django.utils.deconstruct import deconstructible
@deconstructible
class MyValidator:
    def __init__(self, item):
        self.item = item

    def __call__(self, value):
        """ still cant do self.item.minbid
        the object is just a FOREIGN_KEY """
        if value < 10 :
            raise ValidationError('Bid must be at least $10')

class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MyValidator(item)])

    def __str__(self):
        return f'Bid for {self.item.name} : ${self.price}'