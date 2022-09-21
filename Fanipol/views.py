from django.shortcuts import render


def fanipol_view(request):
    return render(request, 'about_fanipol.html', {})


def registration_view(request):
    return render(request, 'registration_rules.html', {})
