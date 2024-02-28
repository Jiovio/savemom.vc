from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Mother
import uuid
from django.http import JsonResponse
import random
import string
import secrets
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignupForm
from .forms import SignupForm, UserLoginForm
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('dashboard')  # Change 'dashboard' to your desired URL name.
            else:
                # Return an 'invalid login' error message.
                pass  # Handle invalid login case
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
def user_management(request):
    users = CustomUser.objects.all()
    return render(request, 'usermanagement.html', {'users': users})
def initiate_video_call(request):
    mothers = Mother.objects.all()  # Retrieve all Mother objects from the database
    return render(request, 'initiate_video_call.html', {'mothers': mothers})
def generate_random_string(length=8):
    """Generate a random string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def start_video_call(request, mother_id=None):
    if request.method == 'GET':
        # Generate a unique room URL for the video call
        room_url = generate_random_string()
        mom = Mother.objects.all()

        # Get the mother object if mother_id is provided
        mother = None
        if mother_id:
            try:
                mother = Mother.objects.get(mother_id=mother_id)
            except Mother.DoesNotExist:
                pass  # Handle the case where mother_id doesn't exist

        return render(request, 'start_video_call.html', {'room_url': room_url, 'mother': mother, 'mom': mom})
    else:
        # Handle POST requests if needed
        pass
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')
            else:
                # Authentication failed, display error message
                error_message = "Invalid username or password."
                return render(request, 'user_login.html', {'form': form, 'error_message': error_message})
        else:
            # Form is not valid, display form with errors
            return render(request, 'user_login.html', {'form': form})
    else:
        # If request method is not POST, display empty login form
        form = UserLoginForm()
        return render(request, 'user_login.html', {'form': form})

def user_dashboard(request):
    if request.user.is_authenticated:
        # Render user dashboard
        return render(request, 'user_dashboard.html')
    else:
        return redirect('user_login')
    
