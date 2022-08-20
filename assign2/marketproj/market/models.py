from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    emailid = models.CharField(max_length= 50,unique=True)
    password = models.CharField(max_length= 60)
    budget = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.username}"

class Item(models.Model):
    itemname = models.CharField(max_length=20)
    barcode = models.IntegerField(default="98765",unique=True)
    price = models.IntegerField()
    desc = models.CharField(default="DESCRIPTION",max_length=1024,unique=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.itemname},{self.barcode},{self.price}"