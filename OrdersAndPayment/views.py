from django.shortcuts import render
from .models import Payment
from .models import Order
from .models import Order_Detail

# Create your views here.

def showPayments(request):

    payments = Payment.objects.all()

    context = {
        'all_payments': payments
    }

    return render(request, 'Orders&Payment/showpayments.html', context)

def showOrders(request):

    orders = Order.objects.all()

    context = {
        'all_orders': orders
    }

    return render(request, 'Orders&Payment/showorders.html', context)

def showOrderDetails(request):

    order_details = Order_Detail.objects.all()

    context = {
        'all_': order_details
    }

    return render(request, 'Orders&Payment/showorderdetails.html', context)