from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product

def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})  # Get the cart from the session
        if not cart:
            return redirect('product_list')  # Redirect if the cart is empty

        # Create a new order
        order = Order.objects.create(user=request.user, total_price=0)
        total_price = 0

        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)  # Get the product
            price = product.price * quantity
            total_price += price

            # Create an OrderItem
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

            # Deduct the quantity from stock
            product.quantity -= quantity
            product.save()

        # Update the order's total price
        order.total_price = total_price
        order.save()

        # Clear the cart
        request.session['cart'] = {}

        return redirect('product_list')  # Redirect to the product list
    return render(request, 'orders/checkout.html')

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})  # Retrieve the cart from the session or create a new one
    cart[product_id] = cart.get(product_id, 0) + 1  # Increment the quantity of the product
    request.session['cart'] = cart  # Save the cart back to the session
    return redirect('product_list')  # Redirect to the product list page