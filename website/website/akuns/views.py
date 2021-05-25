from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from .forms import SignUpForm

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            return redirect("akuns:signin")
    else:
        form = SignUpForm()
    return render(request, "akuns/create_account.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profiles:account_status")
    else:
        form = AuthenticationForm()
    return render(request, "akuns/sign_in.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("akuns:signin")
