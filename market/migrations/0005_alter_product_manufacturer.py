# Generated by Django 4.2.1 on 2023-06-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_cart_options_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=200, verbose_name='Производитель'),
        ),
    ]
