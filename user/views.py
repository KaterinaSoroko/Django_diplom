from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse
from classes.models import Classes
from event.models import Event
from user.forms import LoginForm, SignInForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from organization.models import Organization


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


def login_user_view(request):
    contect = {"login_form": LoginForm()}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('page_user', user.id)
    return render(request, "log_in.html", contect)

def sigh_in_view(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('log_in'))
            except:
                form.add_error(None, "Ошибка")
    else:
        form = SignInForm()
    content = {"form": form}
    return render(request, "sign_in.html", content)

def logout_user_view(request):
    logout(request)
    return redirect(reverse('log_in'))
