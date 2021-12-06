from django.shortcuts import render

from . models import Pizza, Topping

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html') # point to which template to use

def pizza(request):
    pizza = Pizza.objects.order_by('date_added')

    context = {'pizza':pizza}

    return render(request, 'pizzas/pizza.html', context)


def piz(request, piz_id):
    piz = Pizza.objects.get(id=piz_id)

    topping = piz.topping_set.all()

    context = {'piz':piz, 'topping':topping}

    return render(request, 'pizzas/piz.html', context)
