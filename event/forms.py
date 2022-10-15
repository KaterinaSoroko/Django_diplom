from django import forms
from event.models import Event


class EventForms(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("name_event", "description_event", "address_event", "date_event",
                  "time_event", "age_event", "price_event", "price_reference", "phone_reference",
                  "poster", "publication")
        labels = {
            "name_event": 'Название мероприятия',
            "description_event": 'Описание мероприятия',
            "address_event": 'Адрес проведения',
            "age_event": 'Для кого проводится мероприятие',
            "price_event": 'Цена билета',
            "price_reference": 'Как можно приобрести билет',
            "phone_reference": 'Телефон для справок',
        }

        widgets = {
            "date_event": forms.DateInput(
                format=['%d.%m.%Y'],
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'data-target': '#datetimepicker1',
                })
        }
        help_texts = {
            "date_event": "Введите дату в формате 'ДД.MM.ГГГГ'",
            "time_event": "Введите время в формате 'ЧЧ:ММ'",
            "age_event": "(необязательное)",
            "price_event": "(необязательное)",
            "price_reference": "(необязательное)",
            "phone_reference": "Введите телефон в формате '+375299999999' (необязательное)",
            "publication": "Для отображения на странице мероприятий"
        }
