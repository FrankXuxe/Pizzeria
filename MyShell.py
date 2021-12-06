import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")


import django
django.setup()

from pizzas.models import Pizza, Topping
name = Pizza.objects.all()  # SELECT * FROM Topics

for i in name:
    print(i.id)
    print(i.name)
    print(i.date_added)

t = Pizza.objects.get(id=1)
print(t)

names = t.topping_set.all()

for e in names:
    print(e)
