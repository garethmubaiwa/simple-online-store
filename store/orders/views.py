from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Cart, CartItem
from products.models import Product

def get_or_create_cart(request):
    """Get existing cart or create new one"""
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def add_to_cart(request, product_id):
    """Add product to cart"""
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Check if product already in cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')

def cart_detail(request):
    """Display cart contents"""
    cart = get_or_create_cart(request)
    cart_items = cart.cart_items.all()  # Changed from 'items' to 'cart_items'
    total = sum(item.total_price() for item in cart_items)
    
    return render(request, 'orders/cart_detail.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total': total
    })

def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__session_key=request.session.session_key)
    cart_item.delete()
    return redirect('cart_detail')