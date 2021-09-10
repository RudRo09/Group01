from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product, ReviewRating
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct

# test purpose import
from django.http import JsonResponse

# Create your views here.
def store(request, category_slug=None):
	catagories = None
	products = None

	if category_slug is not None:
		catagories = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=catagories, is_available=True).order_by('id')
		product_count = products.count()
		paginator = Paginator(products, 3)
		page = request.GET.get('page')
		page_products = paginator.get_page(page)

	else:
		products = Product.objects.all().filter(is_available=True).order_by('id')
		product_count = products.count()
		paginator = Paginator(products, 3)
		page = request.GET.get('page')
		page_products = paginator.get_page(page)

	context = {
		'products': page_products,
		'product_count': product_count,
	}

	return render(request, 'byteshop/store.html', context)


def product_detail(request, category_slug, product_slug):
	try:
		single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
		in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
	except Exception as e:
		raise e

	try:
		orderproduct = OrderProduct.objects.filter(user=request.user,\
			product_id=single_product.id).exists()
	except OrderProduct.DoesNotExist:
		orderproduct = None

	# getting reviews
	reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)
	context = {
		'single_product': single_product,
		'in_cart': in_cart,
		'orderproduct': orderproduct,
		'reviews': reviews,
	}

	return render(request, 'byteshop/product_detail.html', context)


# search functionalities
def search(request):
	products = None
	product_count = 0

	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			products = Product.objects.order_by('created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
			product_count = products.count()

	if 'term' in request.GET:
		qs = Product.objects.filter(product_name__istartswith=request.GET.get('term'))
		titles = list()
			
		for product in qs:
			titles.append(product.product_name)

		return JsonResponse(titles, safe=False)


	context = {
		'products': products,
		'product_count': product_count,
	}

	return render(request, 'byteshop/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)