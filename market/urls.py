from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('players/', views.PlayersView.as_view(), name='players'),
    path('players/<int:pk>/', views.PlayerDetailView.as_view(), name='player'),
    path('add_to_cart/<int:pk>/', views.AddProductToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', views.RemoveProductFromCartView.as_view(), name='remove_from_cart'),
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name='cart'),
    path('make_order/<int:pk>/', views.MakeOrderView.as_view(), name='make_order'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
