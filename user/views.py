from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse
from user.forms import SignInForm, LoginForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from organization.models import Organization


def page_user_view(request, user_id):
    user_list = User.objects.get(pk=user_id)
    org_list = Organization.objects.filter(username=user_id)
    return render(request, 'page_user.html', {"user_list": user_list, "org_list": org_list})


def login_user_view(request):
    contect = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form.auth(request)
            next_url = request.GET.get("next")
            if next_url is not None:
                return redirect(next_url)
            return redirect(reverse('about_fanipol'))
        contect.update(login_form=login_form)
    return render(request, "log_in.html", contect)


class SighInView(FormView):
    template_name = "sign_in.html"
    form_class = SignInForm

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        return reverse("log_in")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def logout_user_view(request):
    logout(request)
    return redirect(reverse('log_in'))
