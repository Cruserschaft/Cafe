from django import forms
from manager.models import UserReservations


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
        widget=forms.DateInput(attrs={
            'type': "text",
            'name': "date",
            'class': "form-control",
            'id': "date",
            'placeholder': "Дата замовлення",
            'data-rule': "minlen:4",
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

    class Meta:
        model = UserReservations
        fields = ('name', 'email', 'phone', 'date_order', 'time_order', 'of_people', 'message')
