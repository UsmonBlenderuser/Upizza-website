from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/<str:sort_by>/<int:amount>/', index, name='homepage'),

    path('search product/', search_product, name='search_p'),
    path('searching product/', searching, name='searching'),

    path('filtering/', filtering, name='filters'),
    path('choose_brands/', branding, name='branding'),
    path('choose_categories/', category_choose, name='categories'),
    path('choose_materials/', material_choose, name='materials'),

    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('cart/', show_cart, name='cart'),
    path('order/', order, name='order'),

    path('about/', about, name='about'),

    path('product/<slug:p_slug>/', product, name='product'),
]