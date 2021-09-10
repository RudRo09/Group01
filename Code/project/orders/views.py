from django.shortcuts import render

# Create your views here.
 def confirm_payment(request):
	if request.method == 'POST':
		form = PaymentForm(request.POST)
 		if form.is_valid():
 			payment_data = Payment()
			payment_data.payment_id = form.cleaned_data['payment_id']
			payment_data.save()

 			return redirect('byteshop')

 	else:
		return render(request, 'orders/confirm_payment.html')