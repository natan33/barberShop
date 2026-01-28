from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("accounts:profile")

    return render(request, "accounts/login.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")
