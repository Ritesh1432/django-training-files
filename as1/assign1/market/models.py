from django.db import models

# Create your models here.
class Item(models.Model):
    itemname = models.CharField(max_length=20)
    barcode = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.itemname} has {self.barcode} and price {self.price}"