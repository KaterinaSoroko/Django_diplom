from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView, DeleteView, ListView
from classes.models import Classes, Photo, Age_list, Age
from classes.forms import ClassesForm, PhotoForm, SearchForm, SearchAgeForm, ChoiceForm, AgeForm
from organization.models import Organization


def page_class_view(request, class_id):
    class_list = get_object_or_404(Classes, pk=class_id)
    org_list = get_object_or_404(Organization, username=class_list.username_id)
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
                    "org_list": org_list,
                    "photo_list": photo_list,
                    "form": form
                })
        else:
            form = PhotoForm()
            return render(request, 'page_class.html', {
                "class": class_list,
                "org_list": org_list,
                "photo_list": photo_list,
                "form": form
            })
    return render(request, 'page_class.html', {"class": class_list, "org_list": org_list, "photo_list": photo_list})


class CreateClassView(View):

    def get(self, request):
        if not self.request.user.is_authenticated:
            return redirect(reverse('log_in'))
        form1 = ClassesForm()
        form2 = ChoiceForm()
        content = {
            "class_form": form1,
            "age_form": form2,
        }
        return render(request, 'create_class.html', content)

    def post(self, request):
        form1 = ClassesForm(self.request.POST, self.request.FILES)
        form2 = ChoiceForm(self.request.POST)
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
                if id_1 < id_2:
                    for age in age_list:
                        if id_1 <= age.id <= id_2:
                            Age.objects.create(age=age, name_class=classes)
                else:
                    Age.objects.create(age=age1, name_class=classes)
                return redirect("page_user", request.user.id)
        content = {
            "class_form": form1,
            "age_form": form2,
        }
        return render(request, 'create_class.html', content)


def create_age_view(request, pk):
    class_list = get_object_or_404(Classes, pk=pk)
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            f_age = form.save(commit=False)
            f_age.name_class = class_list
            f_age.save()
            return redirect("page_user", request.user.id)
    else:
        form = AgeForm()
        return render(request, 'update_delete.html', {
            "title": "Добавление возраста",
            "button": "Добавить возраст",
            "class": class_list,
            "form": form
        })
    return render(request, 'update_delete.html', {
        "title": "Добавление возраста",
        "button": "Добавить возраст",
        "class": class_list,
        "form": form
    })


class ChoiseClass1View(ListView):
    model = Classes
    template_name = 'choise_class.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = SearchForm(self.request.GET)
        context["form2"] = SearchAgeForm(self.request.GET)
        parametr = self.request.GET.copy()
        addres = ""
        for key, value in parametr.items():
            if key != "page":
                addres += f"&{key}={value}"
        context["adress"] = addres
        return context

    @staticmethod
    def valid(dicts, name1):
        flag = False
        value = dicts[name1]
        for i in dicts.values():
            if i != value:
                flag = True
                break
        return flag

    def get_queryset(self):
        classes_list = Classes.objects.filter(publication=True)
        classes_list_1, classes_list_2 = classes_list, classes_list
        form1 = SearchForm(self.request.GET)
        form2 = SearchAgeForm(self.request.GET)
        list_number = set()
        if form1.is_valid():
            cat_dict = form1.cleaned_data
            if self.valid(cat_dict, "cat1"):
                for number, cat in enumerate(cat_dict.values()):
                    if not cat:
                        classes_list_1 = classes_list_1.exclude(name_category_id=(number + 1))
        if form2.is_valid():
            age_dict = form2.cleaned_data
            if self.valid(age_dict, "age1"):
                for number, age in enumerate(age_dict.values()):
                    if age:
                        for classes in (classes_list_2.filter(age__age__id=(number + 1))):
                            list_number.add(classes)
            else:
                for classes in classes_list_2:
                    list_number.add(classes)
        for classes in classes_list_1:
            if classes not in list_number:
                classes_list_1 = classes_list_1.exclude(id=classes.id)
        return classes_list_1


# class ChoiseClassView(View):
#
#     @staticmethod
#     def valid(dicts, name1):
#         flag = False
#         value = dicts[name1]
#         for i in dicts.values():
#             if i != value:
#                 flag = True
#                 break
#         return flag
#
#     @staticmethod
#     def pagination(request, classes_list):
#         paginator = Paginator(classes_list, 8)
#         page_number = request.GET.get('page')
#         return paginator.get_page(page_number)
#
#     def get(self, request):
#         classes_list = Classes.objects.filter(publication=True)
#         form1 = SearchForm()
#         form2 = SearchAgeForm()
#         page_obj = self.pagination(request, classes_list)
#         content = {
#             "form1": form1,
#             "form2": form2,
#             "page_obj": page_obj
#         }
#         return render(request, 'choise_class.html', content)
#
#     def post(self, request):
#         classes_list = Classes.objects.filter(publication=True)
#         classes_list_1, classes_list_2 = classes_list, classes_list
#         form1 = SearchForm(request.POST)
#         form2 = SearchAgeForm(request.POST)
#         list_number = set()
#         if form1.is_valid():
#             cat_dict = form1.cleaned_data
#             if self.valid(cat_dict, "cat1"):
#                 for number, cat in enumerate(cat_dict.values()):
#                     if not cat:
#                         classes_list_1 = classes_list_1.exclude(name_category_id=(number + 1))
#         if form2.is_valid():
#             age_dict = form2.cleaned_data
#             if self.valid(age_dict, "age1"):
#                 for number, age in enumerate(age_dict.values()):
#                     if age:
#                         for classes in (classes_list_2.filter(age__age__id=(number + 1))):
#                             list_number.add(classes)
#             else:
#                 for classes in classes_list_2:
#                     list_number.add(classes)
#         for classes in classes_list_1:
#             if classes not in list_number:
#                 classes_list_1 = classes_list_1.exclude(id=classes.id)
#         page_obj = classes_list_1
#         content = {
#             "form1": form1,
#             "form2": form2,
#             "page_obj": page_obj
#         }
#         return render(request, 'choise_class.html', content)


class UpdateClassesView(UpdateView):
    model = Classes
    form_class = ClassesForm
    template_name = 'update_in_form.html'
    extra_context = {
        "title": "Изменение занятия",
        "text": "Внесите изменения:",
        "button": "Сохранить изменения",
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class UpdatePubClassesView(UpdateView):
    model = Classes
    fields = ('publication',)
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Публикация",
        "text": "Вы уверены, что хотите изменить статус?",
        "button": "Изменить статус"
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class DeleteClassesView(DeleteView):
    model = Classes
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Удаление занятия",
        "text": "Вы уверены, что хотите удалить занятие?",
        "button": "Удалить занятие",
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class DeleteAgeView(DeleteView):
    model = Age
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Удаление записи",
        "text": "Вы уверены, что хотите удалить запись о возрасте?",
        "button": "Удалить запись",
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class DeletePhotoView(DeleteView):
    model = Photo
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Удаление фотографии",
        "text": "Вы уверены, что хотите удалить фотографию?",
        "button": "Удалить фотографию",
    }

    def get_success_url(self):
        print(str(self.request))
        return reverse("page_user", kwargs={"user_id": self.request.user.id})
