from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

def auth_view(request):
    signup_form = CustomUserCreationForm()
    login_form = CustomAuthenticationForm(request)

    if request.method == 'POST':
        if 'signup_submit' in request.POST:
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                messages.success(request, "Account created successfully! You can now log in.")
                signup_form = CustomUserCreationForm()
            else:
                messages.error(request, "Signup failed. Please fix the errors below.")

        elif 'login_submit' in request.POST:
            login_form = CustomAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()  # safer than authenticate manually
                if user:
                    login(request, user)
                    role = getattr(user, 'role', 'user')  # default fallback
                    if user.is_superuser:
                        return redirect('admin_dashboard')
                    elif role == 'mentor':
                        return redirect('mentor_dashboard')
                    else:
                        return redirect('user_dashboard')
                else:
                    messages.error(request, "Invalid username or password.")

    return render(request, 'registration/login.html', {
        'signup_form': signup_form,
        'login_form': login_form
    })

# Mentor Login and Signup views can be added similarly if needed

def mentor_auth_view(request):
    mentor_signup = MentorCreationForm()
    mentor_login = MentorLoginForm(request)

    if request.method == 'POST':
        if 'mentor_submit' in request.POST:
            mentor_signup = MentorCreationForm(request.POST)
            if mentor_signup.is_valid():
                user = mentor_signup.save(commit=False) 
                user.role = 'mentor' 
                user.save() 
                
                messages.success(request, "Mentor account created successfully! You can now log in.")
                mentor_signup = MentorCreationForm() 
            else:
                messages.error(request, "Signup failed. Please fix the errors below.")

        elif 'mlogin_submit' in request.POST:
            mentor_login = MentorLoginForm(request, data=request.POST)
            if mentor_login.is_valid():
                user = mentor_login.get_user()
                if user:
                    role = getattr(user, 'role', 'user')
                    if user.is_superuser:
                        login(request, user)
                        return redirect('admin_dashboard')
                    elif role == 'mentor':
                        login(request, user)
                        return redirect('mentor_dashboard')
                    else:
                        messages.error(request, "This account is not a Mentor account. Please use the general login.")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'registration/mentor_registration.html', {
        'mentor_signup': mentor_signup,
        'mentor_login': mentor_login
    })


@login_required
def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')


@login_required
def mentor_dashboard(request):
    return render(request, 'dashboard/mentor_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')
