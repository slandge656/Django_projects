from django import template
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    print(cart,'carttt')
    keys=cart.keys()
    for key in keys:
        if int(key) == product.id:
            return True
    else:
        return False
    
@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys=cart.keys()
    for key in keys:
        if int(key) == product.id:
            return cart.get(key)
    else:
        return 0

