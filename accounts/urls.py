from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import registr


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registr/', registr, name='registr'),
]
