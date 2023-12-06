from .models import Zayaka
from django.forms import ModelForm, TextInput

class Zayaka_form(ModelForm):
    class Meta:
        model = Zayaka
        fields = ['number', 'closing_time', 'gruz',
                  'transport', 'kolishestvo', 'pogruzka', 'razgruzka']

        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholdar': '№ Груза'
            }),
            "closing_time": TextInput(attrs={
                'class': 'form-control-plaintext',
                'placeholdar': 'Время до закрытия'
            }),
            "gruz": TextInput(attrs={
                'class': 'form-control-plaintext',
                'placeholdar': 'Груз'
            }),
            "transport": TextInput(attrs={
                'class': 'form-control-plaintext',
                'placeholdar': 'Транспорт'
            }),
            "kolishestvo": TextInput(attrs={
                'class': 'form-control-plaintext',
                'placeholdar': 'Количество'
            }),
            "pogruzka": TextInput(attrs={
                'class': 'form-control-plaintext',
                'placeholdar': 'Погрузка'
            }),
            "razgruzka": TextInput(attrs={
                'class': 'form-control-plaintext',
                'placeholdar': 'Разгрузка'
            })
        }