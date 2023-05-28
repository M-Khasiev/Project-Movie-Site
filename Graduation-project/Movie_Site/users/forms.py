from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField(label='Введите текст с картинки')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {'first_name': 'Имя'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'log'})
