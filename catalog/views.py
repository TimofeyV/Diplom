from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product
from .forms import AddForm
from django.utils.text import slugify
from unidecode import unidecode


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('?')[:5]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'catalog/list.html',
                  {'category': category, 'categories': categories,
                   'products': products,})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'catalog/detail.html',
                  {'product': product, })


def add_product(request):  
    
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)              
        if form.is_valid():
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            time = form.cleaned_data['time']
            price = form.cleaned_data['price']
            
            slug = slugify(unidecode(name))
            print(slug)
            new_product = Product(name = name, slug = slug ,description=description, image=image , category= category , 
                                  time= time, price = price)
            new_product.save()
            return redirect('catalog:product_list')
    else:      
        form = AddForm()
        context = {'form': form}
        return render(request, 'catalog/add_form.html', context )


def edit_product(request, id):

    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            time = form.cleaned_data['time']
            price = form.cleaned_data['price']
            steps = form.cleaned_data['steps']
            slug = slugify(unidecode(name))
            new_product = Product(name = name, slug = slug,  description=description, image=image , category= category ,
                                  time= time, price = price, steps = steps)
            new_product.save()
            return redirect('catalog:product_list')


    else:
        form = AddForm(instance=product)
        context = {'form': form}
        return render(request, 'catalog/add_form.html', context )