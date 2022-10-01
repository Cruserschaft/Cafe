from django import forms
from Cafe import settings
from manager.models import UserReservations
import re


# use forms.Form where don't use db
class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        min_length=4,
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "name",
            'class': "form-control",
            'id': "name",
            'placeholder': "Ваше Ім'я",
            'data-rule': "minlen:4",
            'data-msg': "Ім'я має містити не менше 4х символів",
        })
    )

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "email",
        'class': "form-control",
        'name': "email",
        'id': "email",
        'placeholder': "Емейл",
        'data-rule': "email",
        'data-msg': "Введіть дійсній Емейл",
    }))

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': "text",
            'class': "form-control",
            'name': "phone",
            'id': "phone",
            'placeholder': "Номер телефону",
            'data-rule': "minlen:10",
            'data-msg': "Номер телефону має містити не менше 10 символів",
        }))

    date_order = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(attrs={
            'type': "text",
            'name': "date",
            'class': "form-control",
            'id': "date",
            'placeholder': "Дата замовлення",
            'data-rule': "minlen:6",
            'data-msg': "Введіть коректну дату",
        })
    )

    time_order = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': "text",
            'class': "form-control",
            'name': "time",
            'id': "time",
            'placeholder': "Час замовлення",
            'data-rule': "minlen:4",
            'data-msg': "Введіть корректний час",
        })
    )
    of_people = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'type': "number",
            'class': "form-control",
            'name': "people",
            'id': "people",
            'placeholder': "На скільки чоловік?",
            'data-rule': "minlen:1",
            'data-msg': "Введіть кількість місць",
        })
    )

    message = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'name': "message",
            'rows': "5",
            'placeholder': "Додаткове повідомлення",
        })
    )

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(re.findall(r"[A-Za-zА-Яа-яІіЄєЇї\s]{2,30}", data)) == 1:
            return data
        raise forms.ValidationError("Enter a valid name.")

    def clean_email(self):
        data = self.cleaned_data["email"]
        if len(re.findall(r"[A-Za-z.-]{3,10}@[A-Za-z0-9]{4,}.[a-z]{3}", data)) == 1:
            return data
        raise forms.ValidationError("Enter a valid email address.")

    def clean_phone(self):
        data = self.cleaned_data["phone"]
        if len(re.findall(r"(\+380?|380?|0)[0-9]{9}", data)) == 1:
            return data
        raise forms.ValidationError("Enter a valid phone number.")

    def clean_date_order(self):
        data = self.data["date_order"]
        if len(re.findall(r"[0-9]{2}.[0-9]{2}.[0-9]{2,4}", data)) == 1:
            return self.cleaned_data["date_order"]
        raise forms.ValidationError("Enter a valid data.")

    def clean_time_order(self):
        data = self.data["time_order"]
        if len(re.findall(r"[0-9]{2}[.,:][0-9]{2}$", data)) == 1:
            return self.cleaned_data["time_order"]
        raise forms.ValidationError("Enter a valid time.")

    def clean_of_people(self):
        data = self.cleaned_data["of_people"]
        if len(re.findall(r"[0-9]{1,2}", str(data))) == 1:
            return data
        raise forms.ValidationError("Enter a valid of people.")

    class Meta:
        model = UserReservations
        fields = ('name', 'email', 'phone', 'date_order', 'time_order', 'of_people', 'message')
