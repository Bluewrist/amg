import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart= {}
    items =  []
    order =  {'get_cart_total':0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=1)
            total = (product.price * cart[i]['quantity'])
            vat = (15/100 * order["get_cart_total"])
            grand_total = (vat + order["get_cart_total"])

            order["get_cart_total"] += total
            order["get_cart_items"] += cart[i]["quantity"]
            order["get_vat"] = vat 
            order["grand_total"] = grand_total

            item = {
                'product': {
                    'id':product.id,
                    'part_name':product.part_name,
                    'price':product.price,
                    'product_img':product.product_img,
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
                    
                }
            items.append(item)
        except:
            pass
    return {'items': items,'order':order,'cartItems':cartItems}