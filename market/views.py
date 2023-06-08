from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions, generics
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from market.serializers import ProductSerializer, PlayerSerializer, CartSerializer, OrderSerializer
from market.models import Product, ProductType, Player, Game, Cart, Order


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'market/index.html', {'cart': Cart.objects.get(buyer=request.user)})
    else:
        return render(request, 'market/index.html')


class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]

    def get_product_lists(self):
        d = {}
        for product_type in ProductType.objects.all():
            d[product_type] = self.queryset.filter(product_type=product_type)
        return d

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(buyer=request.user) if request.user.is_authenticated else None
        return Response({
            'user': request.user,
            'product_list': self.get_product_lists(),
            'cart': cart,
        },
            template_name=r'market\products.html'
        )

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]

    def check_cart(self, request):
        return Cart.objects.filter(buyer=request.user).first().products.contains(self.get_object())

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(buyer=request.user) if request.user.is_authenticated else None
        return Response({
            'user': request.user,
            'product': self.get_object(),
            'cart': cart,
        },
            template_name=r'market\product_detail.html'
        )


class AddProductToCartView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]

    def check_cart(self, request):
        return Cart.objects.filter(buyer=request.user).first().products.contains(self.get_object())

    def get(self, request, *args, **kwargs):
        user_cart = Cart.objects.get(buyer=request.user)
        user_cart.products.add(self.get_object())
        user_cart.price += self.get_object().price
        user_cart.save()
        return HttpResponseRedirect(redirect_to=f'/products/{self.get_object().id}/')


class RemoveProductFromCartView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]

    def check_cart(self, request):
        return Cart.objects.filter(buyer=request.user).first().products.contains(self.get_object())

    def get(self, request, *args, **kwargs):
        user_cart = Cart.objects.get(buyer=request.user)
        user_cart.products.remove(self.get_object())
        user_cart.price -= self.get_object().price
        user_cart.save()
        if 'cart' in request.META.get('HTTP_REFERER'):
            redirect = f'/cart/{Cart.objects.get(buyer=request.user).id}/'
        if 'products' in request.META.get('HTTP_REFERER'):
            redirect = f'/products/{self.get_object().id}/'
        return HttpResponseRedirect(redirect_to=redirect)


class PlayersView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]

    def get_player_lists(self):
        d = {}
        for game in Game.objects.all():
            d[game] = self.queryset.filter(game=game)
        return d

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(buyer=request.user) if request.user.is_authenticated else None
        return Response({
            'user': request.user,
            'player_list': self.get_player_lists(),
            'cart': cart
        },
            template_name=r'market\players.html'
        )


class PlayerDetailView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]


    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(buyer=request.user) if request.user.is_authenticated else None
        return Response({
            'user': request.user,
            'player': self.get_object(),
            'devices': self.get_object().devices.all(),
            'cart': cart
        },
            template_name=r'market\player_detail.html'
        )


class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]


    def get(self, request, *args, **kwargs):
        return Response({
            'user': request.user,
            'cart': self.get_object(),
        },
            template_name=r'market\cart.html'
        )


class MakeOrderView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]


    def get(self, request, *args, **kwargs):
        order = Order.objects.create(
            buyer=self.get_object().buyer,
            price=self.get_object().price,
        )
        for product in self.get_object().products.all():
            order.products.add(product)
        order.save()
        cart = Cart.objects.get(id=self.get_object().id)
        cart.products.clear()
        cart.price = 0
        cart.save()
        return HttpResponseRedirect(redirect_to='/profile/')



class ProfileView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response({
            'user': request.user,
            'orders': self.get_queryset().filter(buyer=request.user).order_by('date'),
            'cart': Cart.objects.get(buyer=request.user),
        },
            template_name=r'market\profile.html'
        )

