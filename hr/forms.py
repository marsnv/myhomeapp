from hr.models import hr_staff
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput


class hr_createForm(ModelForm):
    class Meta:
        model = hr_staff
        fields = ['LastName', 'Name', 'MiddleName', 'BirthDate', 'Salary']
        widgets = {
            "LastName":TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия: '}),
            "Name":TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя: '}),
            "MiddleName":TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество: '}),
            "BirthDate":DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата рождения: '}),
            "Salary":NumberInput(attrs={'class': 'form-control', 'placeholder': 'Оклад: '}),
        }
