from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Model to allow both vertuo and original coffee ranges
class Range(models.Model):
    name = models.CharField(max_length=35, blank=False)

    def __str__(self):
        return self.name

# Model to allow 1-10 intensity 
class Intensity(models.Model):
    intensity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.intensity)

# Main coffee model which has name,description and image. Also has intensity and range as foreign keys
class Coffee(models.Model):
    name = models.CharField(max_length=40, blank=False)
    intensity = models.ForeignKey(Intensity,default=1, on_delete=models.CASCADE)
    overview = models.CharField(max_length=200, blank=False, default=1)
    image = models.ImageField(upload_to='img')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    coffee_range = models.ForeignKey(Range, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='review')
    author = models.ForeignKey(User, related_name='coffeecomment')
    text = models.TextField(blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
