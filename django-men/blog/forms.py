from .models import Post, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    # Pozbyłem się help text bo krzyczy, że hasłą zbyt słabe (a mają być )
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, help_text='')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username_or_email = forms.CharField(label="Username or Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


# Znalazłem inne rozwiązanie bez 'Meta' i sprawdzam je.
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old password", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirm new password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
