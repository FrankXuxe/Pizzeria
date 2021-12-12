from django.contrib import admin

# Register your models here.
from .models import Comment, Pizza, Topping, Image

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)
admin.site.register(Image)