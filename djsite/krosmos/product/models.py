from django.db import models


class Images(models.Model):

    image = models.ImageField(upload_to='product/%Y/%m/%d/', verbose_name='Фото')

    belongs_to = models.ForeignKey(
        'Product',
        related_name='images',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Принадлежит'
    )

    def __str__(self):
        return str(self.belongs_to)

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'


class Materials(models.Model):

    name = models.CharField(blank=True, max_length=700, verbose_name='Название')
    slug = models.SlugField(blank=True, unique=True, max_length=700, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материал'


class Category(models.Model):

    name = models.CharField(max_length=255, blank=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Brand(models.Model):

    name = models.CharField(max_length=255, blank=True, verbose_name='Имя бренда')
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['name']


class CartItem(models.Model):
    slug = models.SlugField(max_length=255, blank=True, verbose_name='URL Продукта')
    profile_index = models.CharField(max_length=255, blank=True, verbose_name='Индекс(код пользователя)')
    size = models.IntegerField(verbose_name='Размер')
    count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.profile_index

    class Meta:
        verbose_name = 'Выбранные товары'
        verbose_name_plural = 'Выбранные товары'
        ordering = ['profile_index']


class Profileindex(models.Model):
    profile_index = models.CharField(max_length=255, unique=True, verbose_name='index')

    def __str__(self):
        return self.profile_index

    class Meta:
        verbose_name = 'Индексация пользователей'
        verbose_name_plural = 'Индексация пользователей'
        ordering = ['profile_index']


class Product(models.Model):

    male_or = (
        ('men', 'men'),
        ('women', 'women'),
        ('child', 'child'),
    )

    season_or = (
        ('winter', 'winter'),
        ('summer', 'summer'),
        ('demiseason', 'demiseason'),
    )

    title = models.CharField(max_length=255, blank=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name='URL')
    text = models.TextField(blank=True, verbose_name='Описание товара')

    price = models.FloatField(blank=True, default=0.0, verbose_name='Цена')
    sale = models.FloatField(blank=True, default=0.0, verbose_name='Скидка')
    sale_price = models.FloatField(blank=False, default=0.0, verbose_name='Цена по скидке')
    male_type = models.CharField(max_length=60, default='men', choices=male_or, verbose_name='М/Ж')
    season = models.CharField(max_length=60, default='demiseason', choices=season_or, verbose_name='Сезон')
    time_create = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        related_name='product',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )
    materials = models.ManyToManyField(
        Materials,
        blank=False,
        related_name='product',
        verbose_name='Материалы поверхности',
    )
    brand = models.ForeignKey(
        Brand,
        blank=False,
        related_name='product',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Бренд продукта',
    )
    # available_colors = models.ManyToManyField(
    #     'Product',
    #     blank=False,
    #     related_name='product',
    #     verbose_name='Доступные цвета',
    # )

    image = models.ImageField(blank=True, upload_to='product/images/%Y/%m/%d/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):

    profile_index = models.CharField(max_length=700, verbose_name='Индекс профиля')
    address = models.CharField(max_length=700, verbose_name='Адрес')
    phone_number = models.CharField(max_length=300, verbose_name='Номер телефона')

    products = models.TextField(verbose_name='Продукт')

    def __str__(self):
        return self.profile_index

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel/%Y/', verbose_name='Изображение слайда')
    headline = models.CharField(blank=False, default='None', max_length=255, verbose_name='Загаловок(не обязательно)')
    text = models.TextField(blank=False, default='None', verbose_name='Верхний текст(не обязательно)')
    url = models.CharField(max_length=255, blank=False, default='None', verbose_name='URL(не обязательно)')
    urltext = models.CharField(max_length=255, blank=False, default='None', verbose_name='Надпись на кнопке(не обязательно)')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

