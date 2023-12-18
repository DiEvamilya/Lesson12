from django.urls import path

from client.views import product_list_view, product_detail_view, comment_create_view, product_category_view, \
    shop_product_view

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('product-detail/<slug:product_slug>/', product_detail_view, name='product_detail'),
    path('product-detail/<slug:product_slug>/comment-create/', comment_create_view, name='comment_create'),
    path('product_category/<slug:category_slug>', product_category_view, name='product_category'),
    path('shop_product/<slug:shop_slug>/', shop_product_view, name='shop_product'),

]