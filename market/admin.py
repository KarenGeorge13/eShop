from django.contrib import admin
from market.models import Product, ProductType, Game, Player, Cart, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Cart)
admin.site.register(Order)
