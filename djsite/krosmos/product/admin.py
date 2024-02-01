from django.contrib import admin
from .models import *


class ImageAdmin(admin.ModelAdmin):
    search_fields = ['image', ]


class CartAdmin(admin.ModelAdmin):
    search_fields = ['profile_index', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    list_display_links = ['name', ]
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    list_display_links = ['name', ]
    search_fields = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name', ), }


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    list_display_links = ['name', ]
    search_fields = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name', ), }


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'male_type', 'season', 'category', ]
    list_display_links = ['title', ]
    search_fields = ['title', 'male_type', 'season', 'slug']
    prepopulated_fields = {'slug': ('title', ), }


admin.site.register(Images, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Materials, MaterialAdmin)
admin.site.register(Tag)
admin.site.register(Cart, CartAdmin)
admin.site.register(Profileindex)
admin.site.register(CartItem)
admin.site.register(Product, ProductAdmin)
admin.site.register(Carousel)
