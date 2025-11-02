from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','phone_number', 'password1', 'password2')
    
    #Method to remove the Help Texts from passwords and username
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call the parent's init first
        
        # Turn off the username help text
        if 'username' in self.fields:
            self.fields['username'].help_text = None
            self.fields['username'].label = None
        
        # Turn off the password bullet points (on 'password1')
        if 'password1' in self.fields:
            self.fields['password1'].help_text = None
            
        # (Optional) Turn off the password confirmation help text
        if 'password2' in self.fields:
            self.fields['password2'].help_text = None
        
        if 'phone_number' in self.fields:
            self.fields['phone_number'].help_text = None
            
        # Adding placeholders to the form fields
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'}
        )
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email address'}
        )
        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': 'Phone number'}
        )
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Repeat Password'}
        )

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password'}
        )
        

class MentorCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'previous_experience', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call the parent's init first
        
        # Turn off the username help text
        if 'username' in self.fields:
            self.fields['username'].help_text = None
        
        # Turn off the password bullet points (on 'password1')
        if 'password1' in self.fields:
            self.fields['password1'].help_text = None
            
        # (Optional) Turn off the password confirmation help text
        if 'password2' in self.fields:
            self.fields['password2'].help_text = None
            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'mentor'
        if commit:
            user.save()
        return user

class MentorLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)