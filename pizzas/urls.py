from django.urls import path


from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza', views.pizza, name='pizza'),
    path('pizza/<int:piz_id>/', views.piz, name='piz'),
    path('new_comment/<int:piz_id>/', views.new_comment, name='new_comment'),
]
