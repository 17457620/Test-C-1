from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Purchase
from django.utils.dateparse import parse_date

def index(request):
    return render(request, 'instructions.html')

def question1(request):
    orders = None
    customer = None
    if request.method == 'POST':
        customer_id = request.POST.get('customerNum')
        shipped_status = request.POST.get('shipped')

        if customer_id and shipped_status:
            try:
                customer = Customer.objects.get(pk=customer_id)
                orders = Purchase.objects.filter(customerID=customer, shipped=shipped_status)
            except Customer.DoesNotExist:
                customer = None

    return render(request, 'question1.html', {'orders': orders, 'customer': customer})

def edit_order(request, order_id):
    # Retrieve the order object using orderID field, not the primary key
    order = get_object_or_404(Purchase, orderID=order_id)
    
    if request.method == 'POST':
        # Get the updated data from the form
        shipping_date = request.POST.get('shippingDate')
        shipped_status = request.POST.get('shipped')
        
        # Update the order object
        order.shippingDate = shipping_date
        order.shipped = shipped_status
        
        # Save the changes to the database
        order.save()
        
        # Redirect to a success page or the order detail page
        return redirect('order_detail', order_id=order.orderID)
    
    # If the request method is GET, render the form with the current order data
    return render(request, 'edit_order.html', {'order': order})

def order_list(request):
    orders = Purchase.objects.all()  # Get all orders
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Purchase, orderID=order_id)
    return render(request, 'order_detail.html', {'order': order})

def make_order(request):
    if request.method == 'POST':
        # Get the data from the form
        customer_id = request.POST.get('customerID')
        order_id = request.POST.get('orderID')
        order_date = request.POST.get('orderDate')
        shipped_status = request.POST.get('shipped')
        shipping_date = request.POST.get('shippingDate')
        staff_id = request.POST.get('staffID')

        # Retrieve the customer object
        customer = get_object_or_404(Customer, pk=customer_id)

        # Create and save the new order
        new_order = Purchase(
            orderID=order_id,
            customerID=customer,
            orderDate=parse_date(order_date),
            shipped=shipped_status,
            shippingDate=parse_date(shipping_date) if shipping_date else None,
            staffID=staff_id
        )
        new_order.save()

        # Redirect to the order list or a success page
        return redirect('order_list')

    # If the request method is GET, render the form
    return render(request, 'make_order.html')


