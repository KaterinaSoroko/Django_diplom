import re

from django import forms
from django.core.exceptions import ValidationError

from classes.models import Classes, Photo, Category, Age_list


class ClassesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name_category"].empty_label = "Категория не выбрана"

    class Meta:
        model = Classes
        fields = ("name_category", "name_class", "description_class", "address_class",
                  "datatime_class", "age_class", "price_class", "phone_reference", "poster", "publication")
        labels = {
            "name_class": 'Название занятий/кружка/секции',
            "description_class": 'Описание занятий/кружка/секции',
            "address_class": 'Адрес проведения',
            "poster": 'Фотография',
        }
        help_texts = {
            "name_category": "Выберете категорию для дальнейшего поиска",
            "address_class": "(необязательное)",
            "datatime_class": "Введите дни и время проведения занятий (необязательное)",
            "age_class": "(необязательное)",
            "price_class": "(необязательное)",
            "phone_reference": "Введите телефон в формате '+375299999999' (необязательное)",
        }

    def clean_phone_reference(self):
        phone = self.cleaned_data["phone_reference"]
        if not re.fullmatch(r"^(\+375)+[0-9]{9}$", phone):
            raise ValidationError('Телефон введен не корректно')
        return phone


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ("name_photo",)


class SearchForm(forms.Form):
    cat = Category.objects.all()
    if cat.filter(id=1):
        cat1 = forms.BooleanField(required=False, label=cat.get(id=1).name_category)
    else:
        cat1 = forms.BooleanField()
    if cat.filter(id=2):
        cat2 = forms.BooleanField(required=False, label=cat.get(id=2).name_category)
    if cat.filter(id=3):
        cat3 = forms.BooleanField(required=False, label=cat.get(id=3).name_category)
    if cat.filter(id=4):
        cat4 = forms.BooleanField(required=False, label=cat.get(id=4).name_category)
    if cat.filter(id=5):
        cat5 = forms.BooleanField(required=False, label=cat.get(id=5).name_category)
    if cat.filter(id=6):
        cat6 = forms.BooleanField(required=False, label=cat.get(id=6).name_category)
    if cat.filter(id=7):
        cat7 = forms.BooleanField(required=False, label=cat.get(id=7).name_category)
    if cat.filter(id=8):
        cat8 = forms.BooleanField(required=False, label=cat.get(id=8).name_category)
    if cat.filter(id=9):
        cat9 = forms.BooleanField(required=False, label=cat.get(id=9).name_category)
    if cat.filter(id=10):
        cat10 = forms.BooleanField(required=False, label=cat.get(id=10).name_category)
    if cat.filter(id=11):
        cat11 = forms.BooleanField(required=False, label=cat.get(id=11).name_category)
    if cat.filter(id=12):
        cat12 = forms.BooleanField(required=False, label=cat.get(id=12).name_category)
    if cat.filter(id=13):
        cat13 = forms.BooleanField(required=False, label=cat.get(id=13).name_category)
    if cat.filter(id=14):
        cat14 = forms.BooleanField(required=False, label=cat.get(id=14).name_category)
    if cat.filter(id=15):
        cat15 = forms.BooleanField(required=False, label=cat.get(id=15).name_category)


class SearchAgeForm(forms.Form):
    ages = Age_list.objects.all()
    if ages:
        age1 = forms.BooleanField(required=False, label=ages.get(id=1).age_option)
        age2 = forms.BooleanField(required=False, label=ages.get(id=2).age_option)
        age3 = forms.BooleanField(required=False, label=ages.get(id=3).age_option)
        age4 = forms.BooleanField(required=False, label=ages.get(id=4).age_option)
        age5 = forms.BooleanField(required=False, label=ages.get(id=5).age_option)
        age6 = forms.BooleanField(required=False, label=ages.get(id=6).age_option)
        age7 = forms.BooleanField(required=False, label=ages.get(id=7).age_option)
        age8 = forms.BooleanField(required=False, label=ages.get(id=8).age_option)
        age9 = forms.BooleanField(required=False, label=ages.get(id=9).age_option)
        age10 = forms.BooleanField(required=False, label=ages.get(id=10).age_option)
        age11 = forms.BooleanField(required=False, label=ages.get(id=11).age_option)
        age12 = forms.BooleanField(required=False, label=ages.get(id=12).age_option)
        age13 = forms.BooleanField(required=False, label=ages.get(id=13).age_option)
        age14 = forms.BooleanField(required=False, label=ages.get(id=14).age_option)
        age15 = forms.BooleanField(required=False, label=ages.get(id=15).age_option)
        age16 = forms.BooleanField(required=False, label=ages.get(id=16).age_option)
        age17 = forms.BooleanField(required=False, label=ages.get(id=17).age_option)
    else:
        age1 = forms.BooleanField()


class ChoiceForm(forms.Form):
    age_list = Age_list.objects.all()
    age1 = forms.ModelChoiceField(
        queryset=age_list,
        label="Начальный возраст",
        empty_label="Возраст не выбран"
    )
    age2 = forms.ModelChoiceField(
        queryset=age_list,
        label="Конечный возраст",
        empty_label="Возраст не выбран"
    )

    #def is_valid_age2(self):
    #    if age_list:

