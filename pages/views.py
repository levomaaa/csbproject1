from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.forms import AuthenticationForm  
from .forms import ProfileUpdateForm  
from django.contrib.auth import get_user_model  
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from time import time

# FIX: Insecure Design 1/4 --> take the three lines below out of comments
#ATTEMPT_LIMIT = 5
#LOCKOUT_TIME = 30
#attempt_tracker = {}

User = get_user_model()

# FIX: CSRF --> remove the @csrf_exempt below
@csrf_exempt
def login_view(request):  
    if request.method == 'POST':

        # FIX: Insecure Design 2/4 --> take the three lines below out of comments  
        #username = request.POST.get('username')
        #user_attempts = attempt_tracker.get(username, {'count': 0, 'lockout_until': 0})
        #if user_attempts['count'] >= ATTEMPT_LIMIT and time() < user_attempts['lockout_until']:
        #    return HttpResponse("Too many failed attempts. Account locked for 30 seconds.", status=429)

        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():  
            user = form.get_user()  
            login(request, user)  

        # FIX: Insecure Design 3/4 --> take the line below out of comments
        #    attempt_tracker.pop(username, None)

            return redirect('profile', username=user.username)
        
        # FIX: Insecure Design 4/4 --> take the five lines below out of comments
        #else:
        #    user_attempts['count'] += 1
        #    if user_attempts['count'] >= ATTEMPT_LIMIT:
        #        user_attempts['lockout_until'] = time() + LOCKOUT_TIME
        #    attempt_tracker[username] = user_attempts  

    else:  
        form = AuthenticationForm()  
    
    return render(request, 'index.html', {'form': form})  

def logout_view(request):  
    logout(request)  
    return redirect('/')  

# FIX: CSRF --> remove the @csrf_exempt below
@csrf_exempt  
def profile_view(request, username): 
    
    # FIX: Broken Access Control --> take the four lines below out of comments
    #if not request.user.is_authenticated:
    #    return redirect('/')
    #if request.user.username != username:  
    #    return redirect('profile', username=request.user.username)

    user = get_object_or_404(User, username=username)

    if request.method == 'POST':  
        form = ProfileUpdateForm(request.POST, instance=user)  
        if form.is_valid():  
            form.save()  
            return redirect('profile', username=user.username)  
    else:  
        form = ProfileUpdateForm(instance=user)  

    return render(request, 'profile.html', {'form': form, 'user': user})  
