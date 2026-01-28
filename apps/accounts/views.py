from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.accounts.services import create_customer_user
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next', 'core:home'))

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next', 'core:home'))

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save() # O form faz o split do nome
        create_customer_user(user) # O serviço aplica a regra de negócio
        login(request, user)
        return redirect('core:home')
    
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")
