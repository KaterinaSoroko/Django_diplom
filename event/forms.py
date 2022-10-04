from django import forms


class EventForms(forms.Form):
    name_event = forms.CharField(
        label='Название мероприятия',
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    description_event = forms.CharField(
        label='Описание мероприятия',
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}),
    )
    address_event = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    date_event = forms.DateField(
        input_formats=['%d.%m.%Y'],
        label='Дата проведения',
        help_text="Введите дату в формате 'ДД.ММ.ГГГГ'",
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            'size': '40'
        })
    )
    time_event = forms.TimeField(
        label='Время проведения',
        help_text="Введите время в формате 'ЧЧ.ММ'",
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    age_event = forms.CharField(
        label='Для кого проводится мероприятие',
        help_text="(необязательное)",
        required=False,
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    price_event = forms.CharField(
        label='Цена билета',
        help_text="(необязательное)",
        required=False,
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    price_reference = forms.CharField(
        label='Как можно приобрести билет',
        help_text="(необязательное)",
        required=False,
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    phone_reference = forms.CharField(
        label='Телефон для справок',
        help_text="Введите телефон в формате '+375299999999' (необязательное)",
        required=False,
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    poster = forms.ImageField(
        label='Афиша',
    )
