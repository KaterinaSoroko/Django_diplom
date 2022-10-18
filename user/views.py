from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from user.forms import SignInForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from organization.models import Organization
from classes.models import Classes, Age, Age_list
from event.models import Event


def page_user_view(request, user_id):
    if not request.user.is_authenticated:
        return redirect(reverse('log_in'))
    elif user_id is not request.user.pk:
        content = {"text": "Нет прав доступа!"}
        return render(request, 'page_user.html', content)
    user_list = User.objects.get(pk=request.user.pk)
    org_list = Organization.objects.filter(username=request.user.pk)
    class_list = Classes.objects.filter(username=request.user.pk)
    event_list = Event.objects.filter(username=request.user.pk).order_by("date_event")
    event_end = Event.objects.filter(Q(username=request.user.pk) & Q(date_event__lt=datetime.now()))
    age_list = Age.objects.filter(name_class__username_id=request.user.pk)
    age_options = Age_list.objects.all()
    content = {
        "user_list": user_list,
        "org_list": org_list,
        "class_list": class_list,
        "event_list": event_list,
        "event_end": event_end,
        "age_list": age_list,
        "age_options": age_options,
    }
    return render(request, 'page_user.html', content)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "update_in_form.html"
    extra_context = {
        "title": "Войти в профиль",
        "button": "Войти",
    }

    def get_success_url(self):
        return reverse_lazy('about_fanipol')


class RegisterUser(CreateView):
    form_class = SignInForm
    template_name = 'update_in_form.html'
    extra_context = {
        "title": "Регистрация",
        "button": "Зарегистрировать пользователя",
    }
    success_url = reverse_lazy('log_in')


def logout_user_view(request):
    logout(request)
    return redirect(reverse('log_in'))


class UpdateEmailView(UpdateView):
    model = User
    fields = ('email',)
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Email",
        "text": "Введите новый email",
        "button": "Сохранить изменения",
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class PasswordUpdateView(PasswordChangeView):
    template_name = 'update_in_form.html'
    success_url = reverse_lazy("log_in")
    extra_context = {
        "title": "Изменение пароля",
        "button": "Сохранить изменения",
    }


class DeleteUserView(DeleteView):
    model = User
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Удаление пользователя",
        "text": "Вы уверены, что хотите удалить пользователя?",
        "button": "Удалить пользователя",
    }
    success_url = reverse_lazy('about_fanipol')
