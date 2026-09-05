from django.shortcuts import render , redirect
from result.models.post import Phones
from django.shortcuts import get_object_or_404

def Cart(request, id):

    product = get_object_or_404(Phones, id=id)

    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity', 1))

    product_id = str(product.id)

    if product_id in cart:

        cart[product_id] += quantity

    else:

        cart[product_id] = quantity

    request.session['cart'] = cart

    request.session.modified = True

    return redirect('result:cart')


# =========================
# SHOW CART
# =========================

def CartView(request):

    cart = request.session.get('cart', {})

    products = Phones.objects.filter(
        id__in=cart.keys()
    )

    cart_products = []

    total_price = 0

    for product in products:

        quantity = cart[str(product.id)]

        item_total = product.price * quantity

        total_price += item_total

        cart_products.append({

            'product': product,

            'quantity': quantity,

            'item_total': item_total,

        })

    context = {

        'cart_products': cart_products,

        'total_price': total_price,

    }

    return render(
        request,
        'cart.html',
        context
    )