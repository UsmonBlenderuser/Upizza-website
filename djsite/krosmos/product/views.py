from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime
import random
import json

month = datetime.datetime.now().strftime('%m')
alphabet = 'qwertyuiopasdfghjklzxcvbnm0987654321'

def create_profile_index():
    p_index_list = Profileindex.objects.all()
    new_index = ''
    random_size = int(random.randrange(100, 200))
    for ind in range(random_size):
        random_letter = random.randrange(0, len(alphabet)-1)
        new_index += str(alphabet[random_letter])

    if new_index not in p_index_list:
        new_profile_index = Profileindex(profile_index=new_index)
        new_profile_index.save()
        return new_index
    else:
        return create_profile_index()


@csrf_exempt
def arriving_for(item, arr, second_arr):
    lis = []
    for item2 in arr:
        if item2 in second_arr:
            pass
        else:
            lis.append(item2)

    return lis


@csrf_exempt
def index(request, sort_by, amount):
    #
    # all_images = Product.objects.all()
    #
    # for image in all_images:
    #     image_url = str(image.image)
    #     if image_url[0] != 'p':
    #         image.image = image_url[68::]
    #     image.save()
    carousel_images = Carousel.objects.all()
    products = Product.objects.order_by(str(sort_by)).all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    materials = Materials.objects.all()
    product_list = []
    the_list = []
    the_s_list = []
    cleaning = False
    page_number = request.GET.get('page', 1)

    if request.method == 'GET':
        if request.GET.get('cleaning') == 'true':
            cleaning = True

    if str(request.COOKIES.get('prices')) != 'None':
        try:
            start_price, finish_price = str(request.COOKIES.get('prices')).split(' ')
        except:
            start_price = '90'
            finish_price = '40000'
    else:
        start_price = '90'
        finish_price = '40000'

    brand_cookie = ''
    category_cookie = ''
    material_cookie = ''
    male_cookie = ''
    season_cookie = ''
    price_cookie = ''

    if request.method == 'POST':
        male_cookie, season_cookie, price_cookie = cook_males_and_seasons(request)
        for item in brands:
            if str(item.name) in request.POST:
                brand_cookie += item.slug + ' '
                product_list += arriving_for(1, products.filter(brand=item), product_list)
#                print(products.filter(brand=item))
        for item in categories:
            if str(item.name) in request.POST:
                category_cookie += item.slug + ' '
                product_list += arriving_for(1, products.filter(category=item), product_list)
        for item in materials:
            if str(item.name) in request.POST:
                material_cookie += item.slug + ' '
                product_list += arriving_for(1, products.filter(materials=item), product_list)
#    print(product_list)
    if brand_cookie == '':
        brand_cooKies = str(request.COOKIES.get('sort_by_brands'))
        brand_cookie = brand_cooKies if brand_cooKies != 'None' else ''
        if brand_cooKies != 'None':
            for item in brand_cooKies.split(' '):
                if item == '':
                    break
                item_brand = Brand.objects.get(slug=item)
                product_list += arriving_for(1, products.filter(brand=item_brand), product_list)

    if category_cookie == '':
        category_cooKies = str(request.COOKIES.get('sort_by_categories'))
        category_cookie = category_cooKies if category_cooKies != 'None' else ''
        if category_cooKies != 'None':
            for item in category_cooKies.split(' '):
                if item == '':
                    break
                item_brand = Category.objects.get(slug=item)
                product_list += arriving_for(1, products.filter(category=item_brand), product_list)

    if material_cookie == '':
        material_cooKies = str(request.COOKIES.get('sort_by_materials'))
        material_cookie = material_cooKies if material_cooKies != 'None' else ''
        if material_cooKies != 'None':
            for item in material_cooKies.split(' '):
                if item == '':
                    break
                item_brand = Materials.objects.get(slug=item)
                product_list += arriving_for(1, products.filter(materials=item_brand), product_list)

    if len(product_list) == 0:
        product_list = products.all()

    if male_cookie == '':
        male_cookie = str(request.COOKIES.get('males'))
    if season_cookie == '':
        season_cookie = str(request.COOKIES.get('seasons'))
    if price_cookie == '':
        price_cookie = str(request.COOKIES.get('prices'))

    if male_cookie != 'None' and male_cookie != '':
        for item in product_list:
            item_male = str(item.male_type)
            if 'wi' in male_cookie and item_male == 'winter':
                the_list.append(item)
            if 'su' in male_cookie and item_male == 'summer':
                the_list.append(item)
            if 'de' in male_cookie and item_male == 'demiseason':
                the_list.append(item)

    if len(the_list) == 0:
        the_list = product_list[::]

    if season_cookie != '' and season_cookie != 'None':
        for item in the_list:
            item_male = str(item.season)
            if 'wi' in season_cookie and item_male == 'winter':
                the_s_list.append(item)
            if 'su' in season_cookie and item_male == 'summer':
                the_s_list.append(item)
            if 'de' in season_cookie and item_male == 'demiseason':
                the_s_list.append(item)

    if len(the_s_list) == 0:
        the_s_list = product_list[::]

    product_list = the_s_list[::]
    second_p_list = []

    if len(product_list) == 0:
        product_list = products

    for item in product_list:
        # Этот код для облехчения задания для добавленя материалов каждому продукту
        # if len(item.materials.all()) == 0:
        #     random_count = 3
        #     ind = random_count
        #     random_materials = []
        #     while ind >= 0:
        #         random_material = materials[random.randrange(0, len(materials))]
        #         if random_material not in random_materials:
        #             random_materials.append(random_material)
        #             ind -= 1
        #     item.materials.set(random_materials)
        #     item.save()

        if item.price - item.sale * item.price//100 != item.sale_price:
            item.sale_price = item.price - item.sale * item.price//100
            item.save()
        if item.sale_price == 0.0:
            item.sale_price = item.price
            item.save()
        try:
            if int(start_price) <= item.sale_price <= int(finish_price):
                second_p_list.append(item)
        except:
            if 90 <= item.sale_price <= 40000:
                second_p_list.append(item)

    if len(second_p_list) != 0:
        product_list = second_p_list[::]

    if len(product_list) == 0 or cleaning is True:
        product_list = products[::]

    if amount != 0:
        paginator = Paginator(product_list, amount)
        page_number = request.GET.get('page', 1)
        rel = paginator.get_page(page_number)
    else:
        rel = product_list

    result = render(request, 'product/index.html', {
                      'title': "Ufoots",
                      'searchbool': False,
                      'product_list': rel,
                      'now_month': month,
                      'sorting': str(sort_by),
                      'amount': amount,
                      'carousel': carousel_images,
                      'page_number': int(page_number),
                  })

    if str(request.COOKIES.get('profile_index')) == 'None':
        your_index = create_profile_index()
        result.set_cookie('profile_index', your_index)
    if cleaning is False:
        result.set_cookie('sort_by_brands', brand_cookie)
        result.set_cookie('sort_by_categories', category_cookie)
        result.set_cookie('sort_by_materials', material_cookie)
        result.set_cookie('males', male_cookie)
        result.set_cookie('seasons', season_cookie)
        result.set_cookie('prices', price_cookie)
    else:
        result.set_cookie('sort_by_brands', "None")
        result.set_cookie('sort_by_categories', "None")
        result.set_cookie('sort_by_materials', "None")
        result.set_cookie('males', "None")
        result.set_cookie('seasons', "None")
        result.set_cookie('prices', "None")

    return result


@csrf_exempt
def search_product(request):

    return render(request, 'product/index.html',
                  {
                      'title': 'Ufoots',
                      'searchbool': True,
                  })


@csrf_exempt
def searching(request):

    return render(request, 'product/index.html',
                  {
                      'title': request.GET.get('search'),
                      'searchbool': False,
                  })


@csrf_exempt
def product(request, p_slug):

    products = Product.objects.all()

    item = Product.objects.get(slug=p_slug)

    item_images = Images.objects.filter(belongs_to=item)

    images = []
    ind = 1
    for items in item_images:
        items.pk = ind
        images.append(items)
        ind += 1

    random_items = []

    for i in range(0, 5):
        rand_id = random.randrange(0, len(products))
        random_items.append(products[rand_id])

    return render(request, 'product/product.html',
                  {
                      'title': item.title,
                      'searchbool': False,
                      'product': item,
                      'random_products': random_items,
                      'images': images,
                      'sorting': '-time_create',
                      'amount': 40,
                      'now_month': month,
                  })


@csrf_exempt
def filtering(request):
    result = render(request, 'product/filtering.html', {
                  'title': 'Фильтры',
                  'sorting': '-time_create',
                  'amount': 40,
              })
    return result


@csrf_exempt
def branding(request):
    brands = Brand.objects.all()
    return render(request, 'product/filtering2.html',
                  {
                      'title': 'Фильтры',
                      'sorting': 'time_create',
                      'amount': 40,
                      'brands': brands,
                  })


@csrf_exempt
def category_choose(request):
    categories = Category.objects.all()
    return render(request, 'product/filtering3.html',
                  {
                      'title': 'Фильтры',
                      'sorting': 'time_create',
                      'amount': 40,
                      'category': categories,
                  })


@csrf_exempt
def material_choose(request):
    materials = Materials.objects.all()
    return render(request, 'product/filtering4.html',
                  {
                      'title': 'Фильтры',
                      'sorting': 'time_create',
                      'amount': 40,
                      'materials': materials,
                  })


@csrf_exempt
def cook_males_and_seasons(req):

    posts = req.POST

    male_cookie = ""
    season_cookie = ""
    price_cookie = ""

    if 'men' in posts:
        male_cookie += 'me'
    if 'women' in posts:
        male_cookie += ' wo'
    if 'kids' in posts:
        male_cookie += ' ki'
    if 'winter' in posts:
        season_cookie += 'wi'
    if 'summer' in posts:
        season_cookie += ' su'
    if 'demiseason' in posts:
        season_cookie += ' de'

    try:
        price_cookie += str(posts.get('price_ot')) if str(posts.get('price_ot')) != 'None' else '90'
    except Exception as ex:
        price_cookie += '90'

    try:
        price_cookie += ' ' + str(posts.get('price_do')) if str(posts.get('price_do')) != 'None' else '40000'
    except Exception as ex:
        price_cookie += ' ' + '40000'

    return male_cookie, season_cookie, price_cookie


@csrf_exempt
def add_to_cart(request):

    slug = request.GET.get('p_slug')
    p_index = request.COOKIES.get('profile_index')
    size = request.POST.get('size')
    amount = int(request.POST.get('amount'))

    all_carts = CartItem.objects.all()

    if len(all_carts) > 0:
        new_cart1 = all_carts.filter(slug=slug, size=size)
        try:
            new_cart = new_cart1.get(profile_index=p_index)
            new_cart.count += amount
        except Exception as ex:
            new_cart = CartItem(slug=slug, size=size, count=amount, profile_index=p_index)
    else:
        new_cart = CartItem(slug=slug, size=size, count=amount, profile_index=p_index)

    new_cart.save()

    result = index(request=request, amount=40, sort_by='time_create')

    return result


@csrf_exempt
def remove_from_cart(request):

    slug = request.GET.get('slug')
    size = request.GET.get('size')
    p_index = request.COOKIES.get('profile_index')

    if slug != 'Delete_all':
        try:
            item = CartItem.objects.get(slug=slug, size=size)
            item.delete()
        except:
            print('Something was wrong in deleting item from cart')
    else:
        items = CartItem.objects.filter(profile_index=p_index)
        items.delete()
    result = show_cart(request)

    return result


@csrf_exempt
def show_cart(request):
    p_index = request.COOKIES.get('profile_index')
    profile_carts = CartItem.objects.filter(profile_index=p_index)
    cart_list = []
    total_price = 0

    for item in profile_carts:
        try:
            product_item = Product.objects.get(slug=item.slug)
            image = product_item.image
            title = product_item.title
            size = item.size
            amount = item.count
            s_price = product_item.sale_price
            slug = product_item.slug
            sale = product_item.sale

            cart_list.append({'image': image,
                              'title': title,
                              'size': size,
                              'sale': sale,
                              'amount': amount,
                              'price': int(s_price) * int(amount),
                              'slug': slug,
                              })
            total_price += int(s_price) * int(amount)
        except Exception as ex:
            pass


    result = render(request, 'product/cart.html', {
                'title': 'Корзина',
                'sorting': 'time_create',
                'amount': 40,
                'total_price': total_price,
                'cart': cart_list,
            })

    return result


@csrf_exempt
def order(request):

    today = datetime.datetime.now()

    p_index = request.COOKIES.get('profile_index')
    products = CartItem.objects.filter(profile_index=p_index)

    new_ord = Cart(profile_index=p_index)

    new_ord.address = str(request.POST.get('address'))
    new_ord.phone_number = str(request.POST.get('phone'))

    ind = 0
    all_p = ''
    total_price = 0
    for item in products:
        ind += 1
        prod = Product.objects.get(slug=item.slug)
        total_price += int(prod.price)
        all_p += f'\n {ind} | title = {prod.title} | slug = /product/{item.slug}/ | size = {item.size} | count = {item.count} | price = {prod.price}\n'

    new_ord.products = all_p + '\n\n DATE : ' + str(today)
    new_ord.products += '\n\n\n Total price = ' + str(total_price) + ' som'

    new_ord.save()
    return remove_from_cart(request)


@csrf_exempt
def about(request):

    return render(request, 'product/about.html', {
          'title': 'Фильтры',
          'sorting': 'time_create',
          'amount': 40,
    })

