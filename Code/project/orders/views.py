from django.shortcuts import render, redirect
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm, PaymentForm
from .models import Order, Payment
from django.contrib import messages

import datetime
import random


# Create your views here.
def place_order(request, total=0, quantity=0):
	current_user = request.user

	# if cart count zero, redirecting back to store page
	cart_items = CartItem.objects.filter(user=current_user)
	cart_count = cart_items.count()
	if cart_count <= 0:
		return redirect('byteshop')

	for cart_item in cart_items:
		total += (cart_item.product.price * cart_item.quantity)
		quantity += cart_item.quantity

	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			# store information inside order table
			order_data = Order()
			order_data.user = current_user
			order_data.first_name = form.cleaned_data['first_name']
			order_data.last_name = form.cleaned_data['last_name']
			order_data.email = form.cleaned_data['email']
			order_data.phone_number = form.cleaned_data['phone_number']
			order_data.address = form.cleaned_data['address']
			order_data.city = form.cleaned_data['city']
			order_data.area = form.cleaned_data['area']
			order_data.order_note = form.cleaned_data['order_note']
			order_data.order_total = total
			order_data.ip = request.META.get('REMOTE_ADDR')
			order_data.save()

			# generate unique order number
			year = int(datetime.date.today().strftime('%Y'))
			month = int(datetime.date.today().strftime('%m'))
			day = int(datetime.date.today().strftime('%d'))
			date = datetime.date(year, month, day)
			current_date = date.strftime("%Y%m%d")
			order_number = current_date + str(order_data.id)
			order_data.order_number = order_number

			order_data.save()

			##########
			order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
			context = {
				'order': order,
				'cart_items': cart_items,
				'total': total,
			}

			#########

			payment_data = Payment()
			payment_data.user = current_user
			payment_data.save()
			payment_data.payment_id = random_num() + str('-') + str(payment_data.id)
			payment_data.save()

			order_data.payment = payment_data
			order_data.save()

			print(payment_data.payment_id)
			return render(request, 'orders/payment.html', context)

		else:
			return redirect('checkout')

def confirm_payment(request):
	return render (request, 'orders/confirm_payment.html')

def confirm_order(request):
	current_user = request.user
	# order = Order.objects.get(user=request.user)
	if request.method == 'POST':
		form = PaymentForm(request.POST)
		if form.is_valid():
			try:
				data = form.cleaned_data['payment_id']
				order = Order.objects.get(user=current_user, payment_id=data)
				return render(request, 'orders/success.html')

			except:			
				messages.error(request, 'Wrong Code!')
				return redirect('confirm_payment')


		# else:
		# 	# print('Form is invalid')
		# 	# messages.success(request, 'Wrong Code!')
		# 	# return render(request, 'orders/confirm_order.html')
		# 	return render(request, 'orders/success.html')


def random_num():
	unique_num = ''
	characters = list('0123456789ABCDEF')

	for i in range(9):
		unique_num += random.choice(characters)

	return unique_num