from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            request.session["registered_user"] = form.cleaned_data["username"]
            return redirect("accounts:register_success")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def register_success_view(request):
    return render(request, "accounts/register_success.html", {
        "username": request.session.get('registered_user', "New User")
    })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username_or_email"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("accounts:dashboard")
            form.add_error(None,"Incorrect username or password")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

@login_required
def dashboard_view(request):
    notes_total = request.user.notes.count()

    return render(
        request,
        "accounts/dashboard.html",
        {
            "active_user": request.user.get_username(),
            "notes_total": notes_total,
        },
    )