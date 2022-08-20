from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} stars {self.stars}"