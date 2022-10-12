from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from classes.models import Classes, Photo, Age_list, Age, Category
from classes.forms import ClassesForm, PhotoForm, SearchForm, SearchAgeForm, ChoiceForm
from organization.models import Organization


def page_class_view(request, class_id):
    class_list = get_object_or_404(Classes, pk=class_id)
    photo_list = Photo.objects.filter(name_class=class_id)
    if class_list.username_id == request.user.id:
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                f_photo = form.save(commit=False)
                f_photo.name_class = class_list
                f_photo.save()
                return render(request, 'page_class.html', {
        "class": class_list,
        "photo_list": photo_list,
        "form": form
    })
        else:
            form = PhotoForm()
            return render(request, 'page_class.html', {
                "class": class_list,
                "photo_list": photo_list,
                "form": form
            })
    return render(request, 'page_class.html', { "class": class_list, "photo_list": photo_list})


def create_class_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('log_in'))
    if request.method == 'POST':
        form1 = ClassesForm(request.POST, request.FILES)
        form2 = ChoiceForm(request.POST)
        if form1.is_valid():
            print(form1.cleaned_data)
            if form2.is_valid():
                f_classes = form1.save(commit=False)
                f_classes.username = User.objects.get(username=request.user)
                p_org = Organization.objects.get(username=request.user)
                f_classes.name_org = p_org
                f_classes.save()
                classes = f_classes
                age1 = form2.cleaned_data["age1"]
                age2 = form2.cleaned_data["age2"]
                age_list = Age_list.objects.all()
                id_1 = age_list.get(age_option=age1).id
                id_2 = age_list.get(age_option=age2).id
                for age in age_list:
                    if id_1 <= age.id <= id_2:
                        Age.objects.create(age=age, name_class=classes)
                return redirect("page_org", p_org.id)
    else:
        form1 = ClassesForm()
        form2 = ChoiceForm()
    content = {
        "class_form": form1,
        "age_form": form2,
    }
    return render(request, 'create_class.html', content)


def valid(dict, name1):
    flag = False
    value = dict[name1]
    for i in dict.values():
        if i != value:
            flag = True
            break
    return flag


def choose_class_view(request):
    classes_list = Classes.objects.filter(publication=True)
    if request.method == 'POST':
        form1 = SearchForm(request.POST)
        form2 = SearchAgeForm(request.POST)
        classes_list_1 = classes_list
        classes_list_2 = classes_list
        list_number = set()
        if form1.is_valid():
            cat_dict = form1.cleaned_data
            if valid(cat_dict, "cat1"):
                for number, cat in enumerate(cat_dict.values()):
                    if not cat:
                        classes_list_1 = classes_list_1.exclude(name_category_id=(number+1))
        if form2.is_valid():
            age_dict = form2.cleaned_data
            if valid(age_dict, "age1"):
                for number, age in enumerate(age_dict.values()):
                    if age:
                        for classes in (classes_list_2.filter(age__age__id=(number+1))):
                            list_number.add(classes)
                            print(list_number)
            else:
                for classes in classes_list_2:
                    list_number.add(classes)
        for classes in classes_list_1:
            if classes not in list_number:
                classes_list_1= classes_list_1.exclude(id=classes.id)
        classes_list = classes_list_1
    else:
        form1 = SearchForm()
        form2 = SearchAgeForm()
    content = {
        "class_list": classes_list,
        "form1": form1,
        "form2": form2
    }
    return render(request, 'choose_class.html', content)
