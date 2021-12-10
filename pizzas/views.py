from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import Pizza, Topping

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

    context = {'piz':piz, 'topping':topping, 'comment':comment}

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

            return redirect('pizzas:pizza', piz_id=piz_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'MainApp/new_comment.html', context)
