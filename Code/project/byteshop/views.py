from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
	context = {
		'single_product': single_product,
		'in_cart': in_cart,
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
