from django.forms import ModelForm
from .models import ReviewNews


class ReviewNewForm(ModelForm):
    """Форма отзыва новостей"""
    class Meta:
        model = ReviewNews
        fields = ['body']
        labels = {'body': 'Ваш комментарии*'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border', 'style': 'width: 500px'})
