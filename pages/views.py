from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.forms import AuthenticationForm  
from .forms import ProfileUpdateForm  
from django.contrib.auth import get_user_model  
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@csrf_exempt
def login_view(request):  
    if request.method == 'POST':  
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():  
            user = form.get_user()  
            login(request, user)  
            return redirect('profile', username=user.username)
    else:  
        form = AuthenticationForm()  
    
    return render(request, 'index.html', {'form': form})  

def logout_view(request):  
    logout(request)  
    return redirect('/')  

@csrf_exempt
#@login_required  
def profile_view(request, username): 

    user = get_object_or_404(User, username=username) 
    if request.method == 'POST':  
        form = ProfileUpdateForm(request.POST, instance=user)  
        if form.is_valid():  
            form.save()  
            return redirect('profile', username=user.username) 
    else:  
        form = ProfileUpdateForm(instance=user)  

    return render(request, 'profile.html', {'form': form, 'user': user}) 