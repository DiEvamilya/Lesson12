from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from shop.models import Product, Category, Shopp


def product_create_view(request):
    context = {'category_list': Category.objects.all(),
               'shop_list': Shopp.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        shop_name = request.POST.get('shop_name')

        for field in ['name', 'price', 'quantity', 'category', 'shop_name']:
            if not request.POST.get(field):
                return HttpResponseBadRequest(f"{field} is required.")


        product = Product()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(pk=category)
        product.shop_name = Shopp.objects.set(slug=shop_name)

        product.save()

    return render(request, "shop_side/product_create.html", context)



def product_delete_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    product.delete()
    # context = {'product_list': Product.objects.all()}
    # return render(request, 'client_side/product_list.html', context)
    return redirect("product_list")

def product_update_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(pk=category)

        product.save()
        return redirect('product_list')

    context = {'product': product,
               'category_list': Category.objects.all()}

    return render(request, 'shop_side/product_update.html', context)


