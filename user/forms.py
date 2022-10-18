from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            "username": "",
            "password1": "Ваш пароль должен содержать как минимум 8 символов.",
        }
