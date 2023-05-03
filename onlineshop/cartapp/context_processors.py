from cartapp.models import Cart, CartItem
from cartapp.views import cartID

def counter(request):
    item_count = 0
    if 'admit' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=cartID(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)