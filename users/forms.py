from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Post
from django.contrib.auth import get_user_model

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['profile_photo', 'first_name',  'last_name','email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo', 'first_name', 'last_name','email']
    
    



User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'profile_photo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_photo'].required = False
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'media_type', 'media_file']