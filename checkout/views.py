from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from coffee.models import Coffee
from django.conf import settings
from django.utils import timezone

import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                coffee = get_object_or_404(Coffee, pk=id)
                total += quantity * coffee.price
                order_line_item = OrderLineItem(order = order, product = coffee, quantity = quantity)
                order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount = int(total*100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "Thank you, Your payment was successful!")
                request.session['cart'] = {}
                return redirect(reverse('all_coffee'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, 'checkout.html', {'order_form': order_form, 
                                             'payment_form': payment_form, 
                                             'publishable': settings.STRIPE_PUBLISHABLE
                                             })
