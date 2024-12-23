from django.shortcuts import render,redirect, get_object_or_404
from products.models import Product


def home(request):
    products = Product.objects.all()
    ctx = {'products' : products}
    return render(request, 'index.html', ctx)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product-list.html', {'products': products})

def product_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')

        Product.objects.create(
            title=title,
            short_content=short_content,
            long_content=long_content,
            price=price,
            image=image,
            category=category
        )
        return redirect('products:list')

    return render(request, 'product-create.html')



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product-detail.html', {'product': product})
