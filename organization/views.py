from django.shortcuts import render


def create_org_view(request):
    return render(request, 'create_org.html', {})


def page_org_view(request):
    return render(request, 'page_org.html', {})


def choose_org_view(request):
    return render(request, 'choose_org.html', {})
