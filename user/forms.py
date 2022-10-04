from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    email = forms.CharField(
        label="Электронный адрес",
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'size': '40'})
    )
    password_repeat = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(attrs={'size': '40'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "password": forms.PasswordInput()
        }
# TODO: как изменить названия форм на русский

    def clean(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("password_repeat"):
            raise forms.ValidationError("Invalid form")
        return self.cleaned_data
# TODO: добавить проверку на занятый логин, описание ошибок


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
