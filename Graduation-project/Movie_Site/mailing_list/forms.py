from django import forms
from captcha.fields import CaptchaField
from .models import MailingList


class MailingListForm(forms.ModelForm):
    captcha = CaptchaField(label='')

    class Meta:
        model = MailingList
        fields = ("captcha", "email")
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "editContent", "placeholder": "Введите адрес электронной почты...",
                       "style": "width: 500px; height: 48px;"})
        }
        labels = {
            "email": ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'captcha':
                field.widget.attrs.update({'class': 'log', 'placeholder': 'Введите название с картинки...'})
