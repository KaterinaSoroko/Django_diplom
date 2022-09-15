from django.shortcuts import render


def page_class_view(request):
    return render(request, 'page_class.html', {})


def create_class_view(request):
    return render(request, 'create_class.html', {})


def choose_class_view(request):
    return render(request, 'choose_class.html', {})
