from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)])
    heartrate = models.IntegerField(default=60,validators=[MinValueValidator(0),MaxValueValidator(200)])
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old. "