from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'size': '40'})
    )

    def clean(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.user = user
            return self.cleaned_data
        self.add_error("username", "Проверьте логин")
        self.add_error("password", "Проверьте пароль")
        raise forms.ValidationError("Пользователь не найден")

    def auth(self, request):
        login(request, self.user)
