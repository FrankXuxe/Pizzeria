from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
class Topping(models.Model):
    piz = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.name

class Comment(models.Model):
    piz = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name

class Image(models.Model):
    piz = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    image = models.ImageField()