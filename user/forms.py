from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class SignInForm(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput()
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
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
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
