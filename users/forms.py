from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from cloudinary.forms import CloudinaryFileField


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput())
    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileForm(forms.ModelForm):
    avatar = CloudinaryFileField(
        options={
            "folder": "CulinaryHub/",
            "crop": "limit",
            "width": 250,
            "height": 250,
            "eager": [{"width": 250, "height": 250, "crop": "fill"}],
        }
    )

    class Meta:
        model = Profile
        fields = ["avatar"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].widget = forms.FileInput()
