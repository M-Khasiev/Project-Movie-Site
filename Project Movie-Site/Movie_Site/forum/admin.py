from django.contrib import admin
from .models import QuestionUser, ReviewQuestion


class ReviewQuestionInline(admin.TabularInline):
    """Отзывы к вопросам из форума"""
    model = ReviewQuestion
    extra = 1
    readonly_fields = ("owner", 'created')


class QuestionUserAdmin(admin.ModelAdmin):
    """Вопрос пользователя"""
    list_display = ("user", "question", "created")
    list_display_links = ("user", "question")
    readonly_fields = ("created",)
    inlines = [ReviewQuestionInline]


class ReviewQuestionAdmin(admin.ModelAdmin):
    """Отзывы к вопросам из форума"""
    list_display = ('owner', 'question_user', 'created')
    list_display_links = ('owner', 'question_user')
    list_filter = ('owner', 'created')
    search_fields = ('owner__username', 'created')


admin.site.register(QuestionUser, QuestionUserAdmin)
admin.site.register(ReviewQuestion, ReviewQuestionAdmin)
