# Generated by Django 5.0.1 on 2024-01-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_carousel_urltext_alter_carousel_headline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.AlterField(
            model_name='carousel',
            name='url',
            field=models.CharField(default='None', max_length=255, verbose_name='URL(не обязательно)'),
        ),
    ]
