# Generated by Django 4.2.1 on 2023-06-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_order_cart'),
        ('accounts', '0002_remove_order_products_alter_marketuser_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketuser',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.cart'),
        ),
    ]