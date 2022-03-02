from django.urls import path
from .views import *

app_name = 'customer'
urlpatterns = [
    path('cart/', cart_home, name='cart_list'),
    path('cart/add/<int:id>', cart_add, name='cart_add'),
    path('cart/remove/<int:id>', cart_remove, name='cart_remove'),
    path('cart/delete/<int:id>', cart_delete, name='cart_delete'),
]