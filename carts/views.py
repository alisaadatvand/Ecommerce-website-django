from django.http import HttpResponse
from django.shortcuts import redirect, render
from carts.models import Cart, CartItem
# from django.views.generic import  DeleteView
from store.models import Product
# from django.urls import reverse_lazy

# private function
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        # cria nova sessao
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        # cartid recebe sessionid(cookies)
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request),
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1     
        
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()

    # return HttpResponse(cart_item.product)
    # exit()
    return redirect('cart')

def cart(request, total=0, fulltotal=0, quantity=0, cart_items=None, tax=0):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.all().filter(cart=cart,is_active=True)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            tax = (total * 0.09)
            quantity += cart_item.quantity
    
    except:
        pass
    
    fulltotal = total + tax
    
    context = {
        'tax': tax,
        'total': total,
        'fulltotal': fulltotal,
        'quantity': quantity,
        'cart_items': cart_items,
    }

    return render(request, 'store/cart.html', context)


# class CartDeleteView( DeleteView):
#     model = Cart
#     template_name = 'cart_delete.html'
#     fields = '__all__'
#     success_url = reverse_lazy( 'cart')
