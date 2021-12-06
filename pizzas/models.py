from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
class Topping(models.Model):
    pizza = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
