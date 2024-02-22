from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem

def home(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'ecommerce/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order, created = Order.objects.get_or_create(user=request.user)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.save()
    order = Order.objects.get(user=request.user)
    order.calculate_total_price()
    print(order.total_price)
    order.save()
    return redirect('product_list')

def increase_quantity(request, order_id):
    order_item = OrderItem.objects.get(pk=order_id)
    order_item.quantity += 1
    order_item.save()
    order = Order.objects.get(user=request.user)
    order.calculate_total_price()
    order.save()
    return redirect('view_cart')

def decrease_quantity(request, order_id):
    order_item = OrderItem.objects.get(pk=order_id)
    order_item.quantity -= 1
    order_item.save()
    order = Order.objects.get(user=request.user)
    order.calculate_total_price()
    order.save()
    return redirect('view_cart')

def update_order_quantity(request, order_id):
    if request.method == "POST":
        quantity = request.POST['quantity']
        order_item = OrderItem.objects.get(pk=order_id)
        order_item.quantity += quantity
        order_item.save()
        order = Order.objects.get(user=request.user)
        order.calculate_total_price()
        order.save()
        return redirect('view_cart')
    
def delete_order(request, order_id):
    order = OrderItem.objects.get(id=order_id)
    order.delete()
    return redirect('view_cart')
    

@login_required
def view_cart(request):
    order = Order.objects.get(user=request.user, is_ordered=False)
    order_items = OrderItem.objects.filter()
    price = order.calculate_total_price()
    print(price)
    order.save()
    return render(request, 'ecommerce/view_cart.html', {'order': order, 'order_items': order_items})

@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, is_ordered=False)
    order.is_ordered = True
    order.save()
    return render(request, 'ecommerce/checkout.html', {'order': order})

    