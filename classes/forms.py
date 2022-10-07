from django import forms
from classes.models import Classes


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
