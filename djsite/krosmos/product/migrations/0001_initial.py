# Generated by Django 4.1.5 on 2023-11-28 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя бренда')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='URL Продукта')),
                ('profile_index', models.CharField(blank=True, max_length=255, verbose_name='Индекс(код пользователя)')),
                ('size', models.IntegerField(verbose_name='Размер')),
                ('count', models.IntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Выбранные товары',
                'verbose_name_plural': 'Выбранные товары',
                'ordering': ['profile_index'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=700, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=700, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материал',
            },
        ),
        migrations.CreateModel(
            name='Profileindex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_index', models.CharField(max_length=255, unique=True, verbose_name='index')),
            ],
            options={
                'verbose_name': 'Индексация пользователей',
                'verbose_name_plural': 'Индексация пользователей',
                'ordering': ['profile_index'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('text', models.TextField(blank=True, verbose_name='Описание товара')),
                ('price', models.FloatField(blank=True, default=0.0, verbose_name='Цена')),
                ('sale', models.FloatField(blank=True, default=0.0, verbose_name='Скидка')),
                ('sale_price', models.FloatField(default=0.0, verbose_name='Цена по скидке')),
                ('male_type', models.CharField(choices=[('men', 'men'), ('women', 'women'), ('child', 'child')], default='men', max_length=60, verbose_name='М/Ж')),
                ('season', models.CharField(choices=[('winter', 'winter'), ('summer', 'summer'), ('demiseason', 'demiseason')], default='demiseason', max_length=60, verbose_name='Сезон')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='product/images/%Y/%m/%d/')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.brand', verbose_name='Бренд продукта')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.category', verbose_name='Категория')),
                ('materials', models.ManyToManyField(related_name='product', to='product.materials', verbose_name='Материалы поверхности')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/%Y/%m/%d/', verbose_name='Фото')),
                ('belongs_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='product.product', verbose_name='Принадлежит')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]