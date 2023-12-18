from django.shortcuts import render, redirect, get_object_or_404

from client.models import Comment
from shop.models import Product, Category, Shopp


# Create your views here.
def product_list_view(request):
    context = {'product_list': Product.objects.all(),
               'category_list': Category.objects.all(),
               'shop_list': Shopp.objects.all()}
    return render(request, 'client_side/product_list.html', context)


def product_detail_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product,
               'comment_list': Comment.objects.filter(product=product)}
    return render(request, "client_side/product_detail.html", context)


def product_category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    context = {'product_list': product,
               'category': category}

    return render(request, 'client_side/product_category.html', context=context)


def comment_create_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
    comment = Comment()
    comment.product = product
    comment.username = username
    comment.body = body
    comment.save()
    return redirect("client_side/product_detail.html", product.slug)


def shop_product_view(request, shop_slug):
    shop = Shopp.objects.get(slug=shop_slug)
    product = Product.objects.filter(shop_name=shop)
    context = {'product_list': product,
               'shopp': shop}

    return render(request, 'client_side/shop_product.html', context=context)






















