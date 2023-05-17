from django.forms import ModelForm
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']
        labels = {'body': 'Ваш комментарии*', 'value': 'Оценка*'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border', 'style': 'width: 500px'})
