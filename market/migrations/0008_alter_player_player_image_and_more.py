# Generated by Django 4.2.1 on 2023-06-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_alter_player_player_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_image',
            field=models.ImageField(blank=True, default='images/default_user.png', upload_to='images/', verbose_name='Фото игрока'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='images/default_prod.jpg', upload_to='images/', verbose_name='Изображение товара'),
        ),
    ]