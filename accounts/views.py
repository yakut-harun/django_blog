from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

from .form import RegisterForm, loginForm


# Create your views here.
def login_view(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form': form ,'title':'Giriş yap'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form': form,'title':'Üye ol'})

def logout_view(request):
    logout(request)
    return redirect('home')

