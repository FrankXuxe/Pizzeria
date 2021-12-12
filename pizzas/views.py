from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import Pizza, Topping, Image

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
    comment = piz.comment_set.all()
    image  = Image.objects.get(piz=piz)
    print(image)

    context = {'piz':piz, 'topping':topping, 'comment':comment, 'image':image}

    return render(request, 'pizzas/piz.html', context)

def new_comment(request, piz_id):
    piz = Pizza.objects.get(id=piz_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.piz = piz
            new_comment.save()

            return redirect('pizzas:piz', piz_id=piz_id)

    context = {'form':form, 'piz':piz}
    return render(request, 'pizzas/new_comment.html', context)



'''
    <img src="{% static 'pizzas/meat lover.jpg' %}" alt="Pizzeria" width="700" height="350">

    <img src="{% static 'pizzas/hawaiian.jpg' %}" alt="Pizzeria" width="700" height="350">
    '''