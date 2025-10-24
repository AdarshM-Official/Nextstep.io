from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','phone_number', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)

class MentorCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'previous_experience', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'mentor'
        if commit:
            user.save()
        return user

class MentorLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)