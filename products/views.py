from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from florists.models import Florist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cart.forms import CartAddProductForm

# Create your views here.
def index(request):
    products = Product.objects.all().order_by('-updated').filter(available=True)


    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)


    context = {
        'products': paged_products
    }

    return render(request, 'products/products.html',context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    florist = get_object_or_404(Florist)

    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'florist': florist,
        'cart_product_form': cart_product_form
    }

    return render(request, 'products/product.html', context)

def search(request):
    return render(request, 'products/search.html')