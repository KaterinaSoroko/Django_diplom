from django import forms
from classes.models import Category


class ClassForm(forms.Form):
    name_class = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    description_class = forms.CharField(
        label='Описание',
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    name_category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        help_text="Выберете категорию для дальнейшего поиска",
    )
    address_class = forms.CharField(
        label='Адрес',
        required=False,
        help_text="(необязательное)",
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    datatime_class = forms.CharField(
        label="Время проведения",
        required=False,
        help_text="Введите дни и время проведения занятий (необязательное)",
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    age_class = forms.CharField(
        label="Для кого",
        required=False,
        help_text="(необязательное)",
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    price_class = forms.CharField(
        label="Цена",
        required=False,
        help_text="(необязательное)",
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    phone_reference = forms.CharField(
        label='Телефон',
        required=False,
        help_text="Введите телефон в формате '+375299999999' (необязательное)",
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    poster = forms.ImageField(
        label='Имя файла',
        required=False,
    )
