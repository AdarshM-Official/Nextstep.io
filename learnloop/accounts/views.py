from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

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


@login_required
def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')

@login_required
def mentor_dashboard(request):
    return render(request, 'dashboard/mentor_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')
