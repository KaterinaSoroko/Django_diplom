from django.shortcuts import render, get_object_or_404
from classes.models import Class


def page_class_view(request, class_id):
    class_list = get_object_or_404(Class, pk=class_id)
    return render(request, 'page_class.html', {"class": class_list})


def create_class_view(request):
    return render(request, 'create_class.html', {})


def choose_class_view(request):
    classes_list = Class.objects.all()
    return render(request, 'choose_class.html', {"class_list": classes_list})
