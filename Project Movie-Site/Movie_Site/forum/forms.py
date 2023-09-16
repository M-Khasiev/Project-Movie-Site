from django.forms import ModelForm
from .models import QuestionUser, ReviewQuestion
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ForumAskQuestion(ModelForm):
    question = forms.CharField(widget=CKEditorUploadingWidget(),
                               label='Раскройте суть вопроса в деталях (обязательное поле)',
                               )

    class Meta:
        model = QuestionUser
        fields = ['subject', 'question']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'subject':
                field.widget.attrs.update({'class': 'log', 'placeholder': "Заголовок темы", 'style': 'width: 100%'})


class ReviewQuestionForm(ModelForm):
    class Meta:
        model = ReviewQuestion
        fields = ['body']
        labels = {'body': 'Ваш комментарии*'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control border', 'style': 'width: 500px'})
