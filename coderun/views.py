from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('rle_tool') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def home_view(request):
    if request.user.is_authenticated:
        return redirect('rle_tool')
    return render(request, 'home.html')

@login_required 
def rle_tool_view(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'profile.html')
