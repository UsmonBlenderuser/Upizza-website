# Generated by Django 5.0.1 on 2024-01-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_carousel_headline_alter_carousel_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='urltext',
            field=models.CharField(default='None', max_length=255, verbose_name='Надпись на кнопке(не обязательно)'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='headline',
            field=models.CharField(default='None', max_length=255, verbose_name='Загаловок(не обязательно)'),
        ),
    ]
