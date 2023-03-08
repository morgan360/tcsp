from django.shortcuts import render
from .models import OrderItem
from bookings.models import Booking, Term
from .forms import OrderCreateForm
# from .tasks import order_created
from cart.cart import Cart
import datetime

today_datetime = datetime.datetime.today()
today_date = datetime.date.today()
current_term = Term.objects.filter(start_date__lte=today_date, end_date__gte=today_date)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # term = Term.objects.get(id=1)
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                # Booking Save
                booking = Booking(
                    user=request.user,
                    order=order,
                    product=item['product'],
                    term=current_term.first(),
                )
                booking.save()

            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

# Create your views here.
