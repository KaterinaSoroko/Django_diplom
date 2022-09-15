from django.shortcuts import render


def fanipol_view(request):
    return render(request, 'about_fanipol.html', {})


def registration_view(request):
    return render(request, 'registration_rules.html', {})


def user_view(request):
    return render(request, 'page_user.html', {})


def create_user_view(request):
    return render(request, 'create_user.html', {})
