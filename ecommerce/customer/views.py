from django.shortcuts import render, get_object_or_404, redirect
from administrator.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart_home(request):
    context = {
        'object_list': Cart.objects.filter(user=request.user).select_related('product'),
    }
    return render(request, 'customer/cart/list.html', context)


@login_required
def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart.objects.filter(user=request.user, product=product).first()
    if not cart:
        cart = Cart.objects.create(user=request.user, product=product, quantity=1)
        return redirect('customer:cart_list')
    
    if cart.quantity < 5:
        cart.quantity += 1
        cart.save()
        return redirect('customer:cart_list')


@login_required
def cart_remove(request, id):
    cart = get_object_or_404(Cart, id=id, user=request.user)
    
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
        return redirect('customer:cart_list')
    
    cart.delete()
    return redirect('customer:cart_list')


@login_required
def cart_delete(request, id):
    cart = get_object_or_404(Cart, id=id, user=request.user)
    cart.delete()
    return redirect('customer:cart_list')