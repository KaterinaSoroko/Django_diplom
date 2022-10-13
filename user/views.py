from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from user.forms import SignInForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from organization.models import Organization
from classes.models import Classes
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
    event_list = Event.objects.filter(username=request.user.pk)
    content = {
        "user_list": user_list,
        "org_list": org_list,
        "class_list": class_list,
        "event_list": event_list,
    }
    return render(request, 'page_user.html', content)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "log_in.html"

    def get_success_url(self):
        return reverse_lazy('about_fanipol')


class RegisterUser(CreateView):
    form_class = SignInForm
    template_name = 'sign_in.html'
    success_url = reverse_lazy('log_in')


def logout_user_view(request):
    logout(request)
    return redirect(reverse('log_in'))
