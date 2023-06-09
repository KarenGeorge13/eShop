# Generated by Django 4.2.1 on 2023-06-04 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_order_cart'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AlterField(
            model_name='marketuser',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.cart'),
        ),
        migrations.AlterField(
            model_name='marketuser',
            name='order_list',
            field=models.ManyToManyField(to='market.order'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
