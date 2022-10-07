from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from classes.models import Classes
from classes.forms import ClassesForm
from organization.models import Organization


def page_class_view(request, class_id):
    class_list = get_object_or_404(Classes, pk=class_id)
    return render(request, 'page_class.html', {"class": class_list})


def create_class_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('log_in'))
    if request.method == 'POST':
        form = ClassesForm(request.POST)
        if form.is_valid():
            try:
                f_classes = form.save(commit=False)
                f_classes.username = User.objects.get(username=request.user)
                p_org = Organization.objects.get(username=request.user)
                f_classes.name_org = p_org
                f_classes.save()
                return redirect("page_org", p_org.id)
            except:
                form.add_error(None, "Ошибка добавления мероприятия")
    else:
        form = ClassesForm()
    content = {"class_form": form}
    return render(request, 'create_class.html', content)


def choose_class_view(request):
    classes_list = Classes.objects.all()
    return render(request, 'choose_class.html', {"class_list": classes_list})
