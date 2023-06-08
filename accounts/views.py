from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

from market.models import Cart


# Create your views here.
def registr(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=name, email='', password=password)
            user.save()

            cart = Cart()
            cart.price = 0
            cart.buyer = user
            cart.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(redirect_to='/login/')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})